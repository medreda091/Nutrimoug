from flask import Blueprint, request, redirect

from database.db import connexion

profil = Blueprint("profil", __name__)


@profil.route("/modifier-profil", methods=["POST"])
def modifier_profil():

    user_id = request.form["user_id"]
    taille = request.form["taille"]
    poids = request.form["poids"]
    activite = request.form["activite"]
    objectif = request.form["objectif"]
    allergies = request.form["allergies"]
    preference_alimentaire = request.form["preference_alimentaire"]

    curseur = connexion.cursor()

    curseur.execute(
        """
        UPDATE users
        SET
            taille=%s,
            poids=%s,
            activite=%s,
            objectif=%s,
            allergies=%s,
            preference_alimentaire=%s
        WHERE id=%s
        """,
        (
            taille,
            poids,
            activite,
            objectif,
            allergies,
            preference_alimentaire,
            user_id
        )
    )

    connexion.commit()

    return redirect("/login")