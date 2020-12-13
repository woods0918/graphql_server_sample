from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER as Integer
from sqlalchemy.dialects.mysql import TEXT as Text
from sqlalchemy.dialects.mysql import BOOLEAN as Boolean
from sqlalchemy.dialects.mysql import DATETIME as Datetime
from sqlalchemy.orm import relationship
from app.database import BASE
from datetime import datetime as pyDatetime

class Todo(BASE):
    __tablename__ = "todos"

    id = Column(Integer(unsigned=True), primary_key=True, unique=True, autoincrement=True)
    user_id = Column(
        Integer(unsigned=True), 
        ForeignKey("users.id")
    )
    title = Column(Text)
    description = Column(Text)
    finished = Column(Boolean)
    deadline = Column(Datetime)

    users = relationship("User")

    def __init__(self, user_id: int, title: str, description: str, deadline: pyDatetime):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.finished = False
        self.deadline = deadline