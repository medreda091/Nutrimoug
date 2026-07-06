from flask import Blueprint
from flask import request
from flask import session
from flask import jsonify

from database.db import connexion

planning = Blueprint("planning", __name__)


@planning.route("/planning", methods=["POST"])
def ajouter_planning():

    if "user_id" not in session:

        return jsonify({"success": False})

    recette = request.form["recette"]
    jour = request.form["jour"]
    repas = request.form["repas"]

    curseur = connexion.cursor(dictionary=True)

    curseur.execute(
        """
        SELECT *
        FROM planning_repas
        WHERE user_id=%s
        AND jour=%s
        AND repas=%s
        """,
        (
            session["user_id"],
            jour,
            repas
        )
    )

    existe = curseur.fetchone()

    if existe:

        return jsonify({
            "success": False,
            "message": "Un repas existe déjà pour ce créneau."
        })

    curseur.execute(
        """
        INSERT INTO planning_repas
        (
            user_id,
            recette,
            jour,
            repas
        )
        VALUES(%s,%s,%s,%s)
        """,
        (
            session["user_id"],
            recette,
            jour,
            repas
        )
    )

    connexion.commit()

    return jsonify({
        "success": True
    })


@planning.route("/supprimer_planning", methods=["POST"])
def supprimer_planning():

    if "user_id" not in session:

        return jsonify({"success": False})

    id_planning = request.form["id"]

    curseur = connexion.cursor()

    curseur.execute(
        """
        DELETE FROM planning_repas
        WHERE id=%s
        AND user_id=%s
        """,
        (
            id_planning,
            session["user_id"]
        )
    )

    connexion.commit()

    return jsonify({
        "success": True
    })