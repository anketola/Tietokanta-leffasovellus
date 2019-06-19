from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoryForm(FlaskForm):
    name = StringField("Kategorian nimi", [validators.Length(min=2, max=20, message="Kategorian nimen tulee olla %(min)d - %(max)d merkkiä.")], render_kw={"class": "form-control"})

    class Meta:
        csrf = False