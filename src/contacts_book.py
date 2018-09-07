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

    def remove_contact(self, id_of_contact_to_remove):
        for contact in self.contacts:
            if str(contact.id) == id_of_contact_to_remove:
                self.contacts.remove(contact)

    def update_contact(self, id_of_contact_to_change, name, telephone):
        for contact in self.contacts:
            if str(contact.id) == id_of_contact_to_change:
                contact.name = name
                contact.telephone = telephone
