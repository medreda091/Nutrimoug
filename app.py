from flask import Flask

from routes.auth import auth
from routes.dashboard import dashboard
from routes.poids import poids
from routes.journal import journal
from routes.profil import profil
from routes.favoris import favoris
from routes.planning import planning



app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

app.secret_key = "nutrimoug_secret"

app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(poids)
app.register_blueprint(journal)
app.register_blueprint(profil)
app.register_blueprint(favoris)
app.register_blueprint(planning)

if __name__ == "__main__":
    app.run(debug=True)
