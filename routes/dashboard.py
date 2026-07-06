from datetime import datetime
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
            
            jours = [
                "Lundi",
                "Mardi",
                "Mercredi",
                "Jeudi",
                "Vendredi",
                "Samedi",
                "Dimanche"
            ]

            jour_actuel = jours[datetime.now().weekday()]

            calories_consommees = 0

            proteines_consommees = 0

            glucides_consommes = 0

            lipides_consommes = 0

            for repas in planning:

                for recette in recettes:

                    if repas["recette"] == recette["nom"]:

                        repas["image"] = recette["image"]

                        repas["calories"] = recette["calories"]

                        repas["proteines"] = recette["proteines"]

                        repas["glucides"] = recette["glucides"]

                        repas["lipides"] = recette["lipides"]

                        if repas["jour"] == jour_actuel:

                            calories_consommees += recette["calories"]

                            proteines_consommees += recette["proteines"]

                            glucides_consommes += recette["glucides"]

                            lipides_consommes += recette["lipides"]

                        break

            calories_restantes = max(
                0,
                calories - calories_consommees
            )

            pourcentage_calories = 0 if calories == 0 else min(
                100,
                round(calories_consommees / calories * 100)
            )

            pourcentage_proteines = 0 if proteines == 0 else min(
                100,
                round(proteines_consommees / proteines * 100)
            )

            pourcentage_glucides = 0 if glucides == 0 else min(
                100,
                round(glucides_consommes / glucides * 100)
            )

            pourcentage_lipides = 0 if lipides == 0 else min(
                100,
                round(lipides_consommes / lipides * 100)
            )
            
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

                poids_moyen=poids_moyen,

                calories_consommees=calories_consommees,

                calories_restantes=calories_restantes,

                proteines_consommees=proteines_consommees,

                glucides_consommes=glucides_consommes,

                lipides_consommes=lipides_consommes,

                pourcentage_calories=pourcentage_calories,

                pourcentage_proteines=pourcentage_proteines,

                pourcentage_glucides=pourcentage_glucides,

                pourcentage_lipides=pourcentage_lipides

            )

        return "Email ou mot de passe incorrect"

    return render_template("login.html")