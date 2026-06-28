from flask import Blueprint, request, redirect

from database.db import connexion

journal = Blueprint("journal", __name__)


@journal.route("/ajouter-aliment", methods=["POST"])
def ajouter_aliment():

    user_id = request.form["user_id"]
    repas = request.form["repas"]
    aliment = request.form["aliment"]

    curseur = connexion.cursor()

    curseur.execute(
        """
        INSERT INTO journal_alimentaire
        (user_id, repas, aliment)
        VALUES (%s,%s,%s)
        """,
        (
            user_id,
            repas,
            aliment
        )
    )

    connexion.commit()

    return redirect("/login")