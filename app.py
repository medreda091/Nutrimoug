from flask import Flask

from routes.auth import auth
from routes.dashboard import dashboard
from routes.poids import poids
from routes.journal import journal
from routes.profil import profil

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

app.secret_key = "nutrimoug_secret"

app.register_blueprint(auth)
print(app.static_folder)
print(app.template_folder)
if __name__ == "__main__":
    print("STATIC =", app.static_folder)
    print("TEMPLATES =", app.template_folder)
    app.run(debug=True)