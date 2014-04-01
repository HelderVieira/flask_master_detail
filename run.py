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
from app import User

if __name__ == '__main__':

    db.drop_all()
    db.create_all()
    db.session.add(User(username="Helder"))
    db.session.commit()
    app.run(debug=True)
