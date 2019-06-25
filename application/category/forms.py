from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

# The form is used as part of the admin tools for adding a new category
class CategoryForm(FlaskForm):
    name = StringField("Kategorian nimi", [validators.Length(min=2, max=20, message="Kategorian nimen tulee olla %(min)d - %(max)d merkkiä.")], render_kw={"class": "form-control", "aria-describedby": "nameHelp"})

    class Meta:
        csrf = False

# This form is part of the functionalities for all who have access to the application
# Used in the view for "Selaa elokuvia" to choose to display best entries in a category
class CategoryViewForm(FlaskForm):
    category = SelectField('Kategoria', [validators.DataRequired()], coerce=int, render_kw={"class": "form-control"})
    
    class Meta:
        csrf = False