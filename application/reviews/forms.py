from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, validators

class ReviewForm(FlaskForm):
    rating = IntegerField("Arvosana", [validators.NumberRange(min=1, max=5)])
    reviewtext = TextAreaField("Arvostelun teksti", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False