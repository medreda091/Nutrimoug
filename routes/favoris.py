from flask import Blueprint
from flask import request
from flask import session
from flask import jsonify

from database.db import connexion

favoris = Blueprint("favoris", __name__)


@favoris.route("/favori", methods=["POST"])
def ajouter_favori():

    if "user_id" not in session:

        return jsonify({"success": False})

    recette = request.form["recette"]

    curseur = connexion.cursor(dictionary=True)

    curseur.execute(
        """
        SELECT *
        FROM favoris
        WHERE user_id=%s
        AND recette=%s
        """,
        (
            session["user_id"],
            recette
        )
    )

    favori = curseur.fetchone()

    if favori:

        return jsonify({
            "success": False,
            "message": "Cette recette est déjà dans vos favoris."
        })

    curseur.execute(
        """
        INSERT INTO favoris(user_id, recette)
        VALUES(%s,%s)
        """,
        (
            session["user_id"],
            recette
        )
    )

    connexion.commit()

    return jsonify({"success": True})


@favoris.route("/supprimer_favori", methods=["POST"])
def supprimer_favori():

    if "user_id" not in session:

        return jsonify({"success": False})

    recette = request.form["recette"]

    curseur = connexion.cursor()

    curseur.execute(
        """
        DELETE FROM favoris
        WHERE user_id=%s
        AND recette=%s
        """,
        (
            session["user_id"],
            recette
        )
    )

    connexion.commit()

    return jsonify({"success": True})