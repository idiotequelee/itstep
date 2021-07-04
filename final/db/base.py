from sqlachemy import create_engine
from sqlachemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///database.sqlite', echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
