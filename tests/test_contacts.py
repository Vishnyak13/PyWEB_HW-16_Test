import unittest
from datetime import datetime

from database.create_db import engine, DBSession, session
from database.models import Base, Contact
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.seed import create_fake_contacts, add_contact, get_contact_by_id, get_all_contacts, update_contact, \
    delete_contact, add_phone, add_email, add_address


class TestDatabase(unittest.TestCase):
    def test_engine(self):
        self.assertEqual(engine.url.database, "addressbook.db", "Should be 'addressbook.db'")
        self.assertEqual(engine.url.drivername, "sqlite", "Should be 'sqlite'")
        self.assertEqual(engine.url.query, {}, "Should be empty dict")

    def test_connection(self):
        self.assertTrue(engine.connect(), "Should be True")
        self.assertTrue(session, "Should be True")

    def test_add_contact(self):
        name = "John"
        last_name = "Doe"
        address = "Some address"
        result = add_contact(name, last_name, address)
        assert result == f"Contact {name} {last_name} was added"
        new_contact = session.query(Contact).filter(Contact.first_name == name).first()
        assert new_contact.first_name == name
        assert new_contact.last_name == last_name
        assert new_contact.address == address
        assert new_contact.created_at == datetime.today().date()



