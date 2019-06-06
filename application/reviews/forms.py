from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ReviewForm(FlaskForm):
    rating = StringField("Arvostelun teksti", [validators.Length(min=1, max=144)])
    reviewtext = TextAreaField("Arvosana", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False