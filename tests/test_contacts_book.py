import pytest
import sys
from werkzeug.datastructures import ImmutableMultiDict
sys.path.insert(0, '../src/')
from contact import *
from flask_sqlalchemy import SQLAlchemy
from contact import *
from contacts_book import *
import config, create_app
from settings import db

class TestContactsBook():

    def get_contacts_book(self):
        return ContactsBook()

    def setup_test(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def test_add_contact_to_db(self):
        self.setup_test()
        contact = Contact("Justynka", '12345')
        contacts_book = self.get_contacts_book()
        contacts_book.add_contact(contact)

        assert Contact.query.filter_by(name="Justynka").first()

    def test_remove_contact_from_db(self):
        self.setup_test()
        contact = Contact("Igor", '123456')
        contacts_book = self.get_contacts_book()
        contacts_book.add_contact(contact)
        contacts_book.delete_contact(contact)

        assert not Contact.query.filter_by(name="Igor").first()

    def test_edit_contact_in_db(self):
        self.setup_test()
        contact = Contact('Kozia', '1234567')
        contacts_book = self.get_contacts_book()
        contacts_book.add_contact(contact)
        contact_to_update = Contact.query.filter_by(name="Kozia").first()
        contacts_book.edit_contact(contact_to_update, "Kozia 2", "555")

        assert Contact.query.filter_by(name="Kozia 2").first()
        assert not Contact.query.filter_by(name="Kozia").first()
