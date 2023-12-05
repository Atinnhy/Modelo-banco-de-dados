from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///create.sqlite3") 

Base = declarative_base()

import src.models

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)