import json
from settings import db
import sys
sys.path.append('../')
from src.contact import Contact

class ContactsBook():

    def __init__(self):
        self.contacts = []

    def get_contacts_as_jsons(self):
        contacts = Contact.query.all()
        arrayOfObjects = []
        for contact in contacts:
            contactAsObject = {
                'name': contact.name,
                'telephone': contact.telephone,
                'id': contact.id
            }
            arrayOfObjects.append(contactAsObject)
        return json.dumps(arrayOfObjects)

    def contact_to_json(self, contact):
        contactAsObject = {
            'name': contact.name,
            'telephone': contact.telephone,
            'id': contact.id
        }
        return json.dumps(contactAsObject)

    def get_contacts(self):
        return Contact.query.all()

    def add_contact(self, name, telephone):
        contact = Contact(name, telephone)
        db.session.add(contact)
        db.session.commit()
        return Contact.query.filter_by(name=name).first()

    def delete_contact(self, id):
        contact = Contact.query.filter_by(id=id).first()
        db.session.delete(contact)
        db.session.commit()
        return contact

    def edit_contact(self, idOfEditedContact, new_name, new_telephone):
        contact = Contact.query.filter_by(id=idOfEditedContact).first()
        contact.name = new_name
        contact.telephone = new_telephone
        db.session.commit()
        return self.inform_about_edit(idOfEditedContact, contact.name, contact.telephone)

    def inform_about_edit(self, idOfEditedContact, new_name, new_telephone):
        return {
            'idOfEditedContact': idOfEditedContact,
            'nameAfterEdit': new_name,
            'telephoneAfterEdit': new_telephone
        }
