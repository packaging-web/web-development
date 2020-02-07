from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Date, Integer, String
from app import db

engine = create_engine('sqlite:///packaging.db', echo = True)
db_session = scoped_session(sessionmaker(autocommit = False,
                                         autoflush = False,
                                         bind = engine))
Base = declarative_base()
Base.query = db_session.query_property()

# create tables
def init_db():
    import models
    Base.metadata.create_all(engine)
