from flask import Blueprint, render_template, request, make_response
import json
from models import listProdutos

geralController = Blueprint("geral", __name__)

@geralController.route("/")
def homePage():
    id = request.args.get('id', default=0, type=int)
    cookie = []

    if request.cookies.get('carrinho'):
        cookie = json.loads(request.cookies.get('carrinho'))
    
    if id != 0:
        if id in cookie:
            print("remover")
            cookie.remove(id)
        elif id not in cookie:
            cookie.append(id)

    resp = make_response(render_template("index.html", listaProdutos = listProdutos, carrinho = cookie))
    resp.set_cookie('carrinho', json.dumps(cookie), max_age=60*60*24)
    return resp

@geralController.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@geralController.route("/administracao")
def administracao():
    return render_template("admin.html")

