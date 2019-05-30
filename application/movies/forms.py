from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class MovieForm(FlaskForm):
    name = StringField("Elokuvan nimi", [validators.Length(min=1, max=144)])
    description = TextAreaField("Kuvaus", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False

class EditMovieForm(FlaskForm):
    name = StringField("Elokuvan nimi", [validators.Length(min=1, max=144)])
    description = TextAreaField("Kuvaus", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False