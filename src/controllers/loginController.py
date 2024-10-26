from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from hashlib import sha256
from models import listUsuarios

loginController = Blueprint("login", __name__)

@loginController.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        senha = sha256(request.form["senha"].encode()).hexdigest()
        for usuario in listUsuarios:
            if usuario.nome == user:
                if usuario.senha == senha:
                    session["id"] = usuario.id
                    session["tipo"] = usuario.tipo
                    flash("Bem vindo!", "success")
                    return redirect(url_for("geral.dashboard"))
                else:
                    flash("", "valid")
                    flash("Senha incorreta.", "invalid")
                    return redirect(url_for("login.login"))
        flash("Usuário não encontrado.", "invalid")
        return redirect(url_for("login.login"))    
    return render_template("login.html")

@loginController.route("/logout")
def logout():
    session.pop('id', None)
    session.pop('tipo', None)
    return redirect(url_for("geral.homePage"))

