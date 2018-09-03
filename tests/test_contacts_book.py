import pytest 
import sys
from werkzeug.datastructures import ImmutableMultiDict

sys.path.insert(0, '../src/')

from contacts_book import *
from contact import *

class TestContactsBook():

    def test_contacts_book_has_contacts_list(self):
        contacts_book = ContactsBook()

        assert len(contacts_book.contacts) == 0

    def test_contacts_book_adds_contact(self):
        contacts_book = ContactsBook()
        stubForm = ImmutableMultiDict([('name', 'Justyna'), ('telephone', '123456')])
        contact = Contact(stubForm)
        contacts_book.add_contact(contact)

        assert contacts_book.contacts[0].name == "Justyna"

    def test_contacts_book_returns_all_contacts(self):
        stubForm1 = ImmutableMultiDict([('name', 'Justyna'), ('telephone', '123456')])
        contact1 = Contact(stubForm1)
        stubForm2 = ImmutableMultiDict([('name', 'Igor'), ('telephone', '987654')])
        contact2 = Contact(stubForm2)
        contacts_book = ContactsBook()
        contacts_book.add_contact(contact1)
        contacts_book.add_contact(contact2)
        contacts = contacts_book.get_contacts()

        assert len(contacts) == 2
