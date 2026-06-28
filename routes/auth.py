from flask import Blueprint, render_template, request, session, redirect

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

auth = Blueprint("auth", __name__)


@auth.route("/")
def accueil():
    return render_template("index.html")


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        nom = request.form["nom"]
        email = request.form["email"]
        password = request.form["password"]
        age = request.form["age"]
        sexe = request.form["sexe"]
        taille = request.form["taille"]
        poids = request.form["poids"]
        activite = request.form["activite"]
        objectif = request.form["objectif"]
        allergies = request.form["allergies"]
        preference = request.form["preference_alimentaire"]

        curseur = connexion.cursor()

        curseur.execute("""
        INSERT INTO users
        (
            nom,
            email,
            password,
            age,
            sexe,
            taille,
            poids,
            activite,
            objectif,
            allergies,
            preference_alimentaire
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            nom,
            email,
            password,
            age,
            sexe,
            taille,
            poids,
            activite,
            objectif,
            allergies,
            preference
        ))

        connexion.commit()

        return redirect("/login")

    return render_template("register.html")


@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/login")