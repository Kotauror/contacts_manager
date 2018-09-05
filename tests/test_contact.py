import pytest
import sys
from werkzeug.datastructures import ImmutableMultiDict
sys.path.insert(0, '../src/')
sys.path.append('../')
from flask_sqlalchemy import SQLAlchemy
from contact import *
import config, create_app

class TestContact():

    def test_add_contact_to_db(self):
        contact = Contact("Justynka", '12345')
        db.session.add(contact)
        db.session.commit()

        assert Contact.query.filter_by(name="Justynka").first()

    def test_remove_contact_from_db(self):
        contact = Contact("Igor", '123456')
        db.session.add(contact)
        db.session.commit()
        contact_to_delete = Contact.query.filter_by(name="Igor").first()
        db.session.delete(contact_to_delete)

        assert not Contact.query.filter_by(name="Igor").first()

    def test_edit_contact_in_db(self):
        contact = Contact('Kozia', '1234567')
        db.session.add(contact)
        db.session.commit()
        contact_to_update = Contact.query.filter_by(name="Kozia").first()
        contact_to_update.name = "Kozia 2"
        contact_to_update.telephone = "1111"
        db.session.commit

        assert Contact.query.filter_by(name="Kozia 2").first()
        assert not Contact.query.filter_by(name="Kozia").first()
