from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:pass123@localhost/postgres', echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
