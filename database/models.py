from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    address = Column("address", String(100), nullable=True, default="No address")
    created_at = Column("created_at", Date, nullable=False)
    phone = relationship(
        "Phone", back_populates="contact", cascade="all, delete-orphan"
    )
    email = relationship(
        "Email", back_populates="contact", cascade="all, delete-orphan"
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    phone_number = Column(String(50), nullable=True, default="No phone number")
    contact_id = Column(
        "contact_id", Integer, ForeignKey("contacts.id"), nullable=False
    )
    contact = relationship("Contact", back_populates="phone")


class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=True, default="No email address")
    contact_id = Column(
        "contact_id", Integer, ForeignKey("contacts.id"), nullable=False
    )
    contact = relationship("Contact", back_populates="email")
