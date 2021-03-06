import sys
sys.path.append('../')
from settings import db

class Contact(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    telephone = db.Column(db.String(120), unique=True)
    __table_args__ = {'extend_existing': True}


    def __init__(self, name, telephone):
        self.name = name
        self.telephone = telephone

    def __repr__(self):
        return '<Contact %r>' % self.name
