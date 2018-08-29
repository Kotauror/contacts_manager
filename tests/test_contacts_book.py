import pytest 
import sys

sys.path.insert(0, '../src/')

from contacts_book import *
from contact import *

class TestContactsBook():

    def test_contacts_book_has_contacts_list(self):
        contacts_book = ContactsBook()

        assert len(contacts_book.contacts) == 0

    def test_contacts_book_adds_contact(self):
        contacts_book = ContactsBook()
        contact = Contact("Justyna", 123456)
        contacts_book.add_contact(contact)

        assert contacts_book.contacts[0].name == "Justyna"

    def test_contacts_book_returns_all_contacts(self):
        contacts_book = ContactsBook()
        contact1 = Contact("Justyna", 123456)
        contact2 = Contact("Igor", 987654)
        contacts_book.add_contact(contact1)
        contacts_book.add_contact(contact2)
        contacts = contacts_book.get_contacts()

        print(isinstance(contacts, list))
        assert len(contacts) == 2
