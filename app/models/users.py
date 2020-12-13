from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER as Integer
from sqlalchemy.dialects.mysql import TEXT as Text
from app.database import BASE

class User(BASE):
    __tablename__ = "users"

    id = Column(Integer(unsigned=True), primary_key=True, unique=True, autoincrement=True)
    name = Column(Text)

    def __init__(self, name: str):
        self.name = name
        