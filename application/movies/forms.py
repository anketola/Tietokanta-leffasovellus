from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, IntegerField, TextAreaField, validators

class MovieForm(FlaskForm):
    name = StringField("Elokuvan nimi", [validators.Length(min=1, max=144)])
    released = IntegerField("Julkaisuvuosi", [validators.NumberRange(min=1800, max=2100)])
    description = TextAreaField("Kuvaus", [validators.Length(min=2, max=144)])
    category = SelectMultipleField('Kategoriat', [validators.DataRequired()], coerce=int)

    class Meta:
        csrf = False

class EditMovieForm(FlaskForm):
    name = StringField("Elokuvan nimi", [validators.Length(min=1, max=144)])
    released = IntegerField("Julkaisuvuosi", [validators.NumberRange(min=1800, max=2100)])
    description = TextAreaField("Kuvaus", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False