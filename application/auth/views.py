from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

# Method for get and post requets for the login function
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

# Method for logging out the current user
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

# Returns the view and form for registering a new user
@app.route("/accounts/new")
def accounts_form():
    return render_template("auth/new.html", form = RegisterForm())

# Method for post request to register a new user
@app.route("/accounts/", methods=["POST"])
def accounts_create():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)
    
    # When creating a new user, the admin column is set as False, creating a normal user 
    # If needed, a new admin has to be created via a direct database access
    a = User(form.username.data, form.password.data, False)

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("index"))

# Returns the view of own page that contains own reviews, access restricted to users (note that admin has this too)
@app.route("/ownpage", methods=["GET"])
@login_required(role="USER")
def accounts_view_own():
    return render_template("auth/ownpage.html", reviews = User.user_reviews_list(current_user.id))