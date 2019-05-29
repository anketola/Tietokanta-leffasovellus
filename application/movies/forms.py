from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class MovieForm(FlaskForm):
    name = StringField("Elokuvan nimi", [validators.Length(min=1)])
    description = TextAreaField("Kuvaus")

    class Meta:
        csrf = False