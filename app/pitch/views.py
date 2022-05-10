from .. import db
from .forms import submitPitch, submitComment
from flask import render_template,redirect,url_for,flash,request
from ..models import User, Pitch, Comment
from . import category
from flask_login import login_required,current_user

@category.route('/pitches')
def pitch():

    pitches = Pitch.query.all()
    pickup_lines = Pitch.query.filter_by(category = 'pickup-lines').all()
    promotion = Pitch.query.filter_by(category = 'promotion').all()
    victory = Pitch.query.filter_by(category = 'victory').all()
    motivation = Pitch.query.filter_by(category = 'motivation').all()
    interview = Pitch.query.filter_by(category = 'interview').all()


    return render_template('pitch/pitch.html', pitches = pitches, pickup_lines = pickup_lines, promotion = promotion, victory = victory, motivation = motivation, interview = interview)

@category.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    new_form = submitPitch()
    if new_form.validate_on_submit():
        category = new_form.category.data
        pitch = new_form.pitch.data
        category = new_form.category.data
        user_id = current_user
        new_pitch_object = Pitch(category=category,pitch = pitch, user_id=current_user._get_current_object().id)
        new_pitch_object.save_p()
        return redirect(url_for('category.pitch'))

    return render_template('pitch/new_pitch.html', new_form = new_form)


@category.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = submitComment()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('pitch/comment.html', form =form, pitch = pitch,all_comments=all_comments)
