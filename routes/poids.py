from flask import Blueprint, request, redirect

from database.db import connexion

poids = Blueprint("poids", __name__)


@poids.route("/ajouter-poids", methods=["POST"])
def ajouter_poids():

    user_id = request.form["user_id"]
    nouveau_poids = request.form["poids"]

    curseur = connexion.cursor()

    curseur.execute(
        """
        INSERT INTO suivi_poids (user_id, poids)
        VALUES (%s,%s)
        """,
        (user_id, nouveau_poids)
    )

    connexion.commit()

    return redirect("/login")