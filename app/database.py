import os
from contextlib import contextmanager
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_CHARSET = os.getenv("DB_CHARSET")

ENGINE = create_engine(
    f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}?charset={DB_CHARSET}"
)
SESSION = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE, expire_on_commit=False)
)

class SelfBase(object):
    def to_dict(self):
        model = {}
        for column in self.__table__.columns:
            model[column.name] = str(getattr(self, column.name))
        return model

BASE = declarative_base(cls=SelfBase)
BASE.query = SESSION.query_property()

@contextmanager
def session_scope():
    session = SESSION()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        