import pytest
import sys
from werkzeug.datastructures import ImmutableMultiDict
sys.path.insert(0, '../src/')
from flask_sqlalchemy import SQLAlchemy
from contacts_book import ContactsBook
import config, create_app
from settings import db

class TestContactsBook():

    def get_contacts_book(self):
        return ContactsBook()

    def setup_test(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def test_return_contacts_as_json(self):
        self.setup_test()
        contacts_book = self.get_contacts_book()
        contacts_book.add_contact("Justynka", '00')
        contacts_book.add_contact("Igus", '11')
        actualResult = contacts_book.get_contacts_as_jsons()
        expectedResult = "[{\"name\": \"Justynka\", \"telephone\": \"00\"}, {\"name\": \"Igus\", \"telephone\": \"11\"}]"

        assert actualResult == expectedResult

    def test_add_contact(self):
        self.setup_test()
        contacts_book = self.get_contacts_book()
        contacts_book.add_contact("Justynka", '12345')

        assert contacts_book.get_contacts()[0].name == "Justynka"

    def test_remove_contact(self):
        self.setup_test()
        contacts_book = self.get_contacts_book()
        contacts_book.add_contact("Igor", "123456")
        contacts_book.delete_contact_by_id(1)

        assert len(contacts_book.get_contacts()) == 0

    def test_edit_contact(self):
        self.setup_test()
        contacts_book = self.get_contacts_book()
        contacts_book.add_contact("Kozia", "1234567")
        contacts_book.edit_contact_by_id(1, "Kozica", "1221")

        assert contacts_book.get_contacts()[0].name == "Kozica"
        assert contacts_book.get_contacts()[0].telephone == "1221"
