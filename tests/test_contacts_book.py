import pytest 
import sys

sys.path.insert(0, '../src/')

from contacts_book import *

class TestContactsBook():

    def test_contacts_book_has_contacts_list(self):
        contacts_book = Contacts_book()
        assert len(contacts_book.contacts) == 0
