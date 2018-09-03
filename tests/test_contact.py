import pytest
import sys
from werkzeug.datastructures import ImmutableMultiDict

sys.path.insert(0, '../src/')

from contact import *

class TestContact():

    def test_contact_has_name(self):
        stubForm = ImmutableMultiDict([('name', 'Justyna'), ('telephone', '123456')])
        contact = Contact(stubForm)

        assert contact.name == "Justyna"

    def test_contact_has_telephone(self):
        stubForm = ImmutableMultiDict([('name', 'Justyna'), ('telephone', '123456')])
        contact = Contact(stubForm)

        assert contact.telephone == '123456'
