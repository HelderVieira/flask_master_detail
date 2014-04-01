#-*- coding: utf-8 -*-
'''
    :Author:
        Helder Vieira da Silva <contato@helder.eti.br>

    :Created:
        2014-04-01

    :License:
        BSD, see LICENSE for more details.
'''
from app import db
from flask.ext.wtf import Form
from models import PhoneNumber
from wtforms import SelectField, TextField, FormField, FieldList, SubmitField, StringField, HiddenField
from wtforms.validators import Optional, Required

class PhoneNumberForm(Form):
    phonetype = SelectField("Type", choices=[(c, c) for c in ['Mobile', 'Home', 'Work', 'Fax', 'Other']])
    number = TextField("Number", validators=[Required()])
    ext = TextField("Notes", validators=[Optional()])
    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(PhoneNumberForm, self).__init__(csrf_enabled=False, *args, **kwargs)

class ModelFieldList(FieldList):
    def __init__(self, *args, **kwargs):         
        self.model = kwargs.pop("model", None)
        super(ModelFieldList, self).__init__(*args, **kwargs)
        if not self.model:
            raise ValueError("ModelFieldList requires model to be set")

    def populate_obj(self, obj, name):
        while len(getattr(obj, name)) < len(self.entries):
            newModel = self.model()
            db.session.add(newModel)
            getattr(obj, name).append(newModel)
        while len(getattr(obj, name)) > len(self.entries):
            db.session.delete(getattr(obj, name).pop())
        super(ModelFieldList, self).populate_obj(obj, name)

class UserForm(Form):
    username = TextField("Username", validators=[Required()])
    phone = ModelFieldList(FormField(PhoneNumberForm), model=PhoneNumber, min_entries=1)
    submit = SubmitField("Submit")
