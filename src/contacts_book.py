import sys
sys.path.append('../')
from settings import db

class ContactsBook():

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        db.session.add(contact)
        db.session.commit()

    def delete_contact(self, contact):
        db.session.delete(contact)
        db.session.commit()

    def edit_contact(self, contact, name, telephone):
        contact.name = name
        contact.telephone = telephone
        db.session.commit()
