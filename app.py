#-*- coding: utf-8 -*-
'''
    :Author:
        Helder Vieira da Silva <contato@helder.eti.br>

    :Created:
        2014-04-01

    :License:
        BSD, see LICENSE for more details.
'''
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % os.path.join(basedir, 'app.db')

app.config['SECRET_KEY'] = '6945712387f7a9ab5b73ddfc12a3c7fd1bc8144165d7fe488f8733093676ssse'

db = SQLAlchemy(app)

from models import User, PhoneNumber

from views import index
