from typing import Dict, Optional
from app.database import session_scope
from app.models.users import User

def insert_user(name: str) -> User:
    user = User(name)
    with session_scope() as session:
        session.add(user)
        session.flush()
        return user

def fetch_user(id: Optional[int]=None, name: Optional[str]=None):
    with session_scope() as session:
        query = session.query(User)
        if id:
            query = query.filter(User.id == id)
        if name:
            query = query.filter(User.name == name)
        return query.all()
