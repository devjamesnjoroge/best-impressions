from .. import db
from .forms import submitPitch
from flask import render_template,redirect,url_for,flash,request
from ..models import User, Pitch
from . import pitch

@pitch.route('/pitches')
def pitch():

    pitches = Pitch.query.all()
    pickup_lines = Pitch.query.filter_by(category = 'pickup-lines').all()
    promotion = Pitch.query.filter_by(category = 'promotion').all()
    victory = Pitch.query.filter_by(category = 'victory').all()
    motivation = Pitch.query.filter_by(category = 'motivation').all()
    interview = Pitch.query.filter_by(category = 'interview').all()


    return render_template('pitch/pitch.html', pitches = pitches, pickup_lines = pickup_lines, promotion = promotion, victory = victory, motivation = motivation, interview = interview)
