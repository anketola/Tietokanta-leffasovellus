from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField, validators

class ReviewForm(FlaskForm):
    rating = RadioField("Arvosana", coerce=int, choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")], validators=[validators.Required()])
    reviewtext = TextAreaField("Arvostelun teksti", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False