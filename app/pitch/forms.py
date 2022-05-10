from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField
from wtforms.validators import DataRequired
from ..models import User, Pitch
from wtforms import ValidationError

CATEGORY_CHOICES = [('pickup_lines', 'pickup-lines'), ('interview', 'interview'), ('promotion', 'promotion'), ('victory', 'victory'), ('motivation', 'motivation')]

class submitPitch(FlaskForm):
    category = SelectField(u'Choose a category for your pitch', choices=CATEGORY_CHOICES, validators = [DataRequired()])
    submit = SubmitField('Submit Pitch')
