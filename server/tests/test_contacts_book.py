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
        expectedResult = "[{\"name\": \"Justynka\", \"telephone\": \"00\", \"id\": 1}, {\"name\": \"Igus\", \"telephone\": \"11\", \"id\": 2}]"

        assert actualResult == expectedResult

    def test_return_single_contact_as_json(self):
        self.setup_test()
        contacts_book = self.get_contacts_book()
        contact = contacts_book.add_contact("Justynka", '00')
        actualResult = contacts_book.contact_to_json(contact)
        expectedResult = "{\"name\": \"Justynka\", \"telephone\": \"00\", \"id\": 1}"

        assert actualResult == expectedResult

    def test_add_contact(self):
        self.setup_test()
        contacts_book = self.get_contacts_book()
        contact = contacts_book.add_contact("Justynka", '12345')

        assert contact.name == "Justynka"
        assert contacts_book.get_contacts()[0].name == "Justynka"

    def test_remove_contact(self):
        self.setup_test()
        contacts_book = self.get_contacts_book()
        contacts_book.add_contact("Igor", "123456")
        contacts_book.delete_contact_by_name("Igor")

        assert len(contacts_book.get_contacts()) == 0

    def test_edit_contact_by_name_both_values(self):
        self.setup_test()
        contacts_book = self.get_contacts_book()
        contacts_book.add_contact("Igor", "123456")
        actual = contacts_book.edit_contact_by_name("Igor", "123456", "Myszek", "9999")
        expected = {
            'oldName': "Igor",
            'newName': "Myszek",
            'newTelephone': "9999"
            }

        assert contacts_book.get_contacts()[0].name == "Myszek"
        assert contacts_book.get_contacts()[0].telephone == "9999"
        assert actual == expected

    def test_edit_contact_by_name_one_value(self):
        self.setup_test()
        contacts_book = self.get_contacts_book()
        contacts_book.add_contact("Igor", "123456")
        actual = contacts_book.edit_contact_by_name("Igor", "123456", "", "9999")
        expected = {
            'oldName': "Igor",
            'newName': "Igor",
            'newTelephone': "9999"
            }

        assert contacts_book.get_contacts()[0].name == "Igor"
        assert contacts_book.get_contacts()[0].telephone == "9999"
        assert actual == expected
