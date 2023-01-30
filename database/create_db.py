from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL_DB = "sqlite:///addressbook.db"

engine = create_engine(URL_DB, echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()
