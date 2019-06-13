from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Salasana", [validators.DataRequired()], render_kw={"class": "form-control"})
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.Length(min=5, max=20, message="Käyttäjänimen pituuden tulee olla %(min)d - %(max)d merkkiä.")], render_kw={"class": "form-control"})
    password = PasswordField("Salasana", [validators.Length(min=5, max=20, message="Salasanan pituuden tulee olla %(min)d - %(max)d merkkiä.")], render_kw={"class": "form-control"})
  
    class Meta:
        csrf = False