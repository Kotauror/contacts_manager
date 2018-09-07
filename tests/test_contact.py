import pytest
import sys
from werkzeug.datastructures import ImmutableMultiDict
sys.path.insert(0, '../src/')
from contact import *
from flask_sqlalchemy import SQLAlchemy
from contact import *
import config, create_app
from settings import db

class TestContact():

    def setup_test(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def test_contact_has_name(self):
        contact = Contact("Justyna", "123")
        assert contact.name == "Justyna"

    def test_contact_has_telephone(self):
        contact = Contact("Justyna", "123")
        assert contact.telephone == "123"

    def test_edit_contact_in_db(self):
        self.setup_test()
        contact = Contact('Kozia', '1234567')
        db.session.add(contact)
        db.session.commit()
        contact_to_update = Contact.query.filter_by(name="Kozia").first()
        contact_to_update.name = "Kozia 2"
        contact_to_update.telephone = "1111"
        db.session.commit()

        assert Contact.query.filter_by(name="Kozia 2").first()
        assert not Contact.query.filter_by(name="Kozia").first()
