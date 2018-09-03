import pytest
import sys
from werkzeug.datastructures import ImmutableMultiDict

sys.path.insert(0, '../src/')

from contact import *

class TestContact():

    def get_contact(self):
        stubForm = ImmutableMultiDict([('name', 'Justyna'), ('telephone', '123456')])
        return Contact(stubForm)

    def test_contact_has_name(self):
        assert self.get_contact().name == "Justyna"

    def test_contact_has_telephone(self):
        assert self.get_contact().telephone == '123456'
