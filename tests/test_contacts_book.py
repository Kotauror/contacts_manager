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
