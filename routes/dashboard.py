from flask import Blueprint, render_template, request, session

from database.db import connexion

from services.nutrition import (
    calculer_imc,
    calculer_calories,
    calculer_macros,
    calculer_eau,
    calculer_conseil
)

from services.menus import generer_menu
from services.recettes import recuperer_recettes
from services.statistiques import calculer_statistiques

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        curseur = connexion.cursor(dictionary=True)

        curseur.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        utilisateur = curseur.fetchone()
        print(email)
        print(password)
        print(utilisateur)

        if utilisateur:

            session["user_id"] = utilisateur["id"]

            poids = float(utilisateur["poids"])
            taille = float(utilisateur["taille"])
            age = int(utilisateur["age"])

            imc, categorie_imc = calculer_imc(
                poids,
                taille
            )

            calories = calculer_calories(
                poids,
                taille,
                age,
                utilisateur["sexe"],
                utilisateur["activite"],
                utilisateur["objectif"]
            )

            proteines, glucides, lipides = calculer_macros(
                calories,
                poids
            )

            eau = calculer_eau(poids)

            conseil = calculer_conseil(imc)

            menu = generer_menu(
                utilisateur["preference_alimentaire"]
            )

            recettes = recuperer_recettes()

            curseur.execute(
                """
                SELECT *
                FROM suivi_poids
                WHERE user_id=%s
                ORDER BY date_mesure DESC
                """,
                (utilisateur["id"],)
            )

            historique = curseur.fetchall()

            historique_graph = list(reversed(historique))

            curseur.execute(
                """
                SELECT *
                FROM journal_alimentaire
                WHERE user_id=%s
                ORDER BY date_ajout DESC
                """,
                (utilisateur["id"],)
            )

            journal = curseur.fetchall()

            poids_min, poids_max, poids_moyen = calculer_statistiques(
                historique
            )

            if poids_min == 0:

                poids_min = poids
                poids_max = poids
                poids_moyen = poids
            
            curseur.execute(
                """
                SELECT recette
                FROM favoris
                WHERE user_id=%s
                """,
                (utilisateur["id"],)
            )

            favoris_db = curseur.fetchall()

            favoris = []

            for favori in favoris_db:

                for recette in recettes:

                    if recette["nom"] == favori["recette"]:

                        favoris.append(recette)

            
            
            curseur.execute(
                """
                SELECT *
                FROM planning_repas
                WHERE user_id=%s
                ORDER BY
                FIELD(
                    jour,
                    'Lundi',
                    'Mardi',
                    'Mercredi',
                    'Jeudi',
                    'Vendredi',
                    'Samedi',
                    'Dimanche'
                )
                """,
                (utilisateur["id"],)
            )

            planning = curseur.fetchall()
            
            return render_template(

                "dashboard.html",

                utilisateur=utilisateur,

                calories=calories,

                proteines=proteines,

                glucides=glucides,

                lipides=lipides,

                eau=eau,

                imc=imc,

                categorie_imc=categorie_imc,

                conseil=conseil,

                menu=menu,

                recettes=recettes,

                favoris=favoris,

                planning=planning,

                historique=historique,

                historique_graph=historique_graph,

                journal=journal,

                poids_min=poids_min,

                poids_max=poids_max,

                poids_moyen=poids_moyen

            )
        return "Email ou mot de passe incorrect"

    return render_template("login.html")