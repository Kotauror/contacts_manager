import sys
import json
sys.path.append('../')
from settings import db
from src.contact import Contact

class ContactsBook():

    def __init__(self):
        self.contacts = []

    def get_contacts_as_jsons(self):
        contacts = Contact.query.all()
        arrayOfObjects = []
        for contact in contacts:
            contactAsObject = {}
            contactAsObject['name'] = contact.name
            contactAsObject['telephone'] = contact.telephone
            contactAsObject['id'] = contact.id
            arrayOfObjects.append(contactAsObject)
        return json.dumps(arrayOfObjects)

    def get_contacts(self):
        return Contact.query.all()

    def contact_to_json(self, contact):
        contactAsObject = {}
        contactAsObject['name'] = contact.name
        contactAsObject['telephone'] = contact.telephone
        contactAsObject['id'] = contact.id
        return json.dumps(contactAsObject)

    def add_contact(self, name, telephone):
        contact = Contact(name, telephone)
        db.session.add(contact)
        db.session.commit()
        return Contact.query.filter_by(name=name).first()

    def delete_contact_by_id(self, id_to_delete):
        contact = Contact.query.filter_by(id=id_to_delete).first()
        db.session.delete(contact)
        db.session.commit()

    def edit_contact_by_id(self, id_to_edit, name, telephone):
        contact = Contact.query.filter_by(id=id_to_edit).first()
        contact.name = name
        contact.telephone = telephone
        db.session.commit()
