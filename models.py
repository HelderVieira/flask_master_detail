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

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50))
    phone = db.relationship(lambda: PhoneNumber)
    
    def __init__(self, username=None):
        self.username=username
    
class PhoneNumber(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    phonetype = db.Column(db.String(10))
    number = db.Column(db.String(20))
    ext = db.Column(db.String(10))
