import pytest 
import sys
from werkzeug.datastructures import ImmutableMultiDict

sys.path.insert(0, '../src/')

from contacts_book import *
from contact import *

class TestContactsBook():

    def get_contact(self):
        stubForm = ImmutableMultiDict([('name', 'Justyna'), ('telephone', '123456')])
        return Contact(stubForm)

    def test_contacts_book_has_contacts_list(self):
        contacts_book = ContactsBook()

        assert len(contacts_book.contacts) == 0

    def test_contacts_book_adds_contact(self):
        contacts_book = ContactsBook()
        contacts_book.add_contact(self.get_contact())

        assert contacts_book.contacts[0].name == "Justyna"

    def test_contacts_book_returns_all_contacts(self):
        contacts_book = ContactsBook()
        contacts_book.add_contact(self.get_contact())
        contacts_book.add_contact(self.get_contact())
        contacts = contacts_book.get_contacts()

        assert len(contacts) == 2

    def test_contacts_book_removes_contacts(self):
        contacts_book = ContactsBook()
        contacts_book.add_contact(self.get_contact())
        id_of_contact = contacts_book.contacts[0].id
        contacts_book.remove_contact(str(id_of_contact))

        assert len(contacts_book.get_contacts()) == 0
