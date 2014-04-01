#-*- coding: utf-8 -*-
'''
    :Author:
        Helder Vieira da Silva <contato@helder.eti.br>

    :Created:
        2014-04-01

    :License:
        BSD, see LICENSE for more details.
'''
from app import app, db
from models import User
from forms import UserForm
from flask import render_template, flash

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"%s - %s" % (
                getattr(form, field).label.text,
                error
            ))

@app.route("/", methods=["GET", "POST"])
def index():
    user = User.query.first()
    form = UserForm(obj = user)
    if form.validate_on_submit():
        form.populate_obj(user)        
        db.session.commit()
    else:
        flash_errors(form)
    return render_template("page.html", form = form)
