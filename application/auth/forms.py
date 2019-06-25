from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

# This form is used for logging in to the application 
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Salasana", [validators.DataRequired()], render_kw={"class": "form-control"})
  
    class Meta:
        csrf = False

# A form used to register a new user
class RegisterForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.Length(min=5, max=20, message="Käyttäjänimen pituuden tulee olla %(min)d - %(max)d merkkiä.")], render_kw={"class": "form-control", "aria-describedby": "usernameHelp"})
    password = PasswordField("Salasana", [validators.Length(min=5, max=20, message="Salasanan pituuden tulee olla %(min)d - %(max)d merkkiä.")], render_kw={"class": "form-control", "aria-describedby": "passwordHelp"})
  
    class Meta:
        csrf = False