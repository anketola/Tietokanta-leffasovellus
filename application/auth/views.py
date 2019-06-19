from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    
    if not form.validate():
        return render_template("auth/loginform.html", form = LoginForm())

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "Väärä käyttäjänimi tai salasana")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/accounts/new")
def accounts_form():
    return render_template("auth/new.html", form = RegisterForm())

@app.route("/accounts/", methods=["POST"])
def accounts_create():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)
    
    a = User(form.username.data, form.password.data, False)

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/ownpage", methods=["GET"])
@login_required(role="USER")
def accounts_view_own():
    return render_template("auth/ownpage.html", reviews = User.user_reviews_list(current_user.id))