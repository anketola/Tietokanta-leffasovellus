from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, IntegerField, TextAreaField, validators

class MovieForm(FlaskForm):
    name = StringField("Elokuvan nimi", [validators.Length(min=1, max=144, message="Elokuvan nimi voi olla pitudeltaan %(min)d - %(max)d merkkiä.")])
    released = IntegerField("Julkaisuvuosi", [validators.NumberRange(min=1800, max=2100, message="Kentän arvon tulee olla välillä %(min)s - %(max)s.")])
    description = TextAreaField("Kuvaus", [validators.Length(min=2, max=1000, message="Kuvauksen tulee olla pituudeltaan %(min)d - %(max)d merkkiä.")])
    category = SelectMultipleField('Kategoriat', [validators.DataRequired()], coerce=int)

    class Meta:
        csrf = False

class EditMovieForm(FlaskForm):
    name = StringField("Elokuvan nimi", [validators.Length(min=1, max=144, message="Kentän pituuden tulee olla %(min)d - %(max)d merkkiä.")])
    released = IntegerField("Julkaisuvuosi", [validators.NumberRange(min=1800, max=2100, message="Kentän arvon tulee olla välillä %(min)s - %(max)s.")])
    description = TextAreaField("Kuvaus", [validators.Length(min=2, max=1000, message="Kentän pituuden tulee olla %(min)d - %(max)d merkkiä.")])
    category = SelectMultipleField('Kategoriat', [validators.DataRequired()], coerce=int)

    class Meta:
        csrf = False