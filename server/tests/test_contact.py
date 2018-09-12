import pytest
import sys
sys.path.insert(0, '../src/')
from contact import *

class TestContact():

    def test_contact_has_name(self):
        contact = Contact("Justyna", "123")
        assert contact.name == "Justyna"

    def test_contact_has_telephone(self):
        contact = Contact("Justyna", "123")
        assert contact.telephone == "123"
