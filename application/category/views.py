from flask import render_template, request, url_for, redirect
from flask_login import current_user

from application import app, db, login_required
from application.category.models import Category
from application.category.forms import CategoryForm

@app.route("/category", methods=["GET"])
@login_required(role="ADMIN")
def category_index():
    return render_template("category/list.html", categories = Category.query.all())

@app.route("/category/new/", methods=["GET"])
@login_required(role="ADMIN")
def category_form():
    return render_template("category/new.html", form = CategoryForm())

@app.route("/category/new", methods=["POST"])
@login_required(role="ADMIN")
def category_create():
    form = CategoryForm(request.form)

    if not form.validate():
        return render_template("category/new.html", form = form)

    c = Category(form.name.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("category_index"))