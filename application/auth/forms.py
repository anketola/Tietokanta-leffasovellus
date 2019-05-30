from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.DataRequired()])
    password = PasswordField("Salasana", [validators.DataRequired()])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.Length(min=6, max=144)])
    password = PasswordField("Salasana", [validators.Length(min=6, max=144)])
  
    class Meta:
        csrf = False