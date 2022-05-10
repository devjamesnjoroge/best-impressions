from .. import db
from .forms import submitPitch
from flask import render_template,redirect,url_for,flash,request
from ..models import User, Pitch
from . import pitch

@pitch.route('/pitch')
def pitch():

    pitch_form = submitPitch()

    return render_template('pitch/pitch.html', pitch_form = pitch_form)
