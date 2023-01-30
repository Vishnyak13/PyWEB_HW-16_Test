import random
import datetime
from faker import Faker
from sqlalchemy.orm import joinedload

from database.create_db import session
from database.models import Contact, Phone, Email

fake = Faker("uk_UA")


def create_fake_contacts(count: int) -> None:
    for _ in range(count):
        contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.address(),
            created_at=fake.date_between(start_date="-1y", end_date="today"),
        )
        session.add(contact)
        session.commit()
        for _ in range(random.randint(1, 2)):
            phone = Phone(phone_number=fake.phone_number(), contact_id=contact.id)
            session.add(phone)
            session.commit()
        for _ in range(random.randint(1, 2)):
            email = Email(email_address=fake.email(), contact_id=contact.id)
            session.add(email)
            session.commit()
    print(f"{count} fake contacts were added in database")


def add_contact(first_name: str, last_name: str, address: str):
    contact = Contact(
        first_name=first_name,
        last_name=last_name,
        address=address,
        created_at=datetime.date.today(),
    )
    session.add(contact)
    session.commit()
    return f"Contact {contact.full_name} was added"


def get_contact_by_id(contact_id):
    contact = (
        session.query(Contact)
        .options(joinedload(Contact.phone), joinedload(Contact.email))
        .filter(Contact.id == contact_id)
        .first()
    )
    phone_numbers = (
        ", ".join([phone.phone_number for phone in contact.phone])
        if contact.phone
        else "No phone number"
    )
    email_addresses = (
        ", ".join([email.email_address for email in contact.email])
        if contact.email
        else "No email"
    )
    return (
        f"Contact: {contact.full_name}, Address: {contact.address},"
        f" Phone: {phone_numbers}"
        f" and Email: {email_addresses}"
        f" was created at {contact.created_at}"
    )


def get_all_contacts():
    contacts = (
        session.query(Contact)
        .options(joinedload(Contact.phone), joinedload(Contact.email))
        .all()
    )
    contacts_list = []
    for contact in contacts:
        phone_numbers = (
            ", ".join([phone.phone_number for phone in contact.phone])
            if contact.phone
            else "No phone number"
        )
        email_addresses = (
            ", ".join([email.email_address for email in contact.email])
            if contact.email
            else "No email"
        )
        contacts_list.append(
            f"Contact: {contact.full_name}, Address: {contact.address},"
            f" Phone: {phone_numbers}"
            f" and Email: {email_addresses}"
            f" was created at {contact.created_at}"
        )
    return "\n".join(contacts_list)


def update_contact(contact_id, first_name, last_name, address):
    contact = session.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = first_name
        contact.last_name = last_name
        contact.address = address
        session.commit()
        return f"Contact {contact.full_name} was updated"
    else:
        return f"Contact with id {contact_id} not found"


def delete_contact(contact_id):
    contact = session.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        session.delete(contact)
        session.commit()
        return f"Contact {contact.full_name} was deleted"
    else:
        return f"Contact with id {contact_id} not found"


def add_phone(contact_id, phone_number):
    contact = session.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        phone = Phone(phone_number=phone_number, contact_id=contact_id)
        session.add(phone)
        session.commit()
        return f"Phone {phone_number} was added to contact {contact.full_name}"
    else:
        return f"Contact with id {contact_id} not found"


def add_email(contact_id, email_address):
    contact = session.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        email = Email(email_address=email_address, contact_id=contact_id)
        session.add(email)
        session.commit()
        return f"Email {email_address} was added to contact {contact.full_name}"
    else:
        return f"Contact with id {contact_id} not found"


def add_address(contact_id, address):
    contact = session.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.address = address
        session.commit()
        return f"Address {address} was added to contact {contact.full_name}"
    else:
        return f"Contact with id {contact_id} not found"
