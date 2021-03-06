from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField, validators

# The form used by registered / logged in users (or admin) to add a review 
class ReviewForm(FlaskForm):
    rating = RadioField("Arvosana", coerce=int, choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")], validators=[validators.Required(message="Valitse arvosana elokuvalle")], render_kw={"class": "form-control"})
    reviewtext = TextAreaField("Arvostelun teksti", [validators.Length(min=2, max=1000, message="Arvostelun pituuden tulee olla %(min)d - %(max)d merkkiä.")], render_kw={"class": "form-control", "cols": "30", "rows": "10"})

    class Meta:
        csrf = False

# As the previous form, but for editing the review entry
class EditReviewForm(FlaskForm):
    rating = RadioField("Arvosana", coerce=int, choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")], validators=[validators.Required(message="Valitse arvosana elokuvalle")], render_kw={"class": "form-control"})
    reviewtext = TextAreaField("Arvostelun teksti", [validators.Length(min=2, max=1000, message="Arvostelun pituuden tulee olla %(min)d - %(max)d merkkiä.")], render_kw={"class": "form-control", "cols": "30", "rows": "10"})

    class Meta:
        csrf = False