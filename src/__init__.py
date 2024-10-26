from flask import Flask, request, session, redirect, url_for, abort, render_template
from controllers import loginController, geralController

app = Flask(__name__)
app.secret_key = "5c30fc3d62f09af83a0a8f914a819ecda3123e3a05bbb338558374cf6c6b6aac"

ROTAS_PUBLICAS = ['geral.homePage', 'login.login', 'static']
ROTAS_ADMIN = ['geral.administracao']

@app.before_request
def authenticate_and_authorize():
    rota = request.endpoint
    if rota in ROTAS_PUBLICAS or rota is None:
        if session.get('id') and rota == "login.login":
            return redirect(url_for("geral.homePage"))
        return
    
    if 'id' not in session:
        abort(401)
    
    if rota in ROTAS_ADMIN:
        if session.get('tipo') != 0:
            abort(403)

app.register_blueprint(geralController)
app.register_blueprint(loginController)

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def pageNotFound(e):
    return render_template("403.html"), 403

@app.errorhandler(401)
def pageNotFound(e):
    return render_template("401.html"), 401

@app.errorhandler(500)
def pageNotFound(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug = True)