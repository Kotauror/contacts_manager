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

    def delete_contact_by_name(self, name_to_delete):
        contact = Contact.query.filter_by(name=name_to_delete).first()
        db.session.delete(contact)
        db.session.commit()
        return contact

    def edit_contact_by_name(self, name_to_edit, newName, newTelephone):
        contact = Contact.query.filter_by(name=name_to_edit).first()
        contact.name = newName
        contact.telephone = newTelephone
        db.session.commit()
        return self.inform_about_edit(name_to_edit, newName, newTelephone)

    def inform_about_edit(self, name_to_edit, newName, newTelephone):
        return {
            'oldName': name_to_edit,
            'newName': newName,
            'newTelephone': newTelephone
        }
