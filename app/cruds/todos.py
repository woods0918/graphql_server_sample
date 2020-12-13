from typing import Dict, Optional
from app.database import session_scope
from app.models.todos import Todo
from datetime import datetime

def insert_todo(user_id: int, title: str, description: str, deadline: datetime) -> Todo:
    todo = Todo(
        user_id=user_id,
        title=title,
        description=description,
        deadline=deadline
    )
    with session_scope() as session:
        session.add(todo)
        session.flush()
        return todo

def fetch_todo(
    id: Optional[int]=None, user_id: Optional[int]=None, title: Optional[str]=None,
    description: Optional[str]=None, deadline: Optional[datetime]=None
):
    with session_scope() as session:
        query = session.query(Todo)
        if id:
            query = query.filter(Todo.id == id)
        if user_id:
            query = query.filter(Todo.user_id == user_id)
        if title:
            query = query.filter(Todo.title == title)
        if description:
            query = query.filter(Todo.description == description)
        if deadline:
            query = query.filter(Todo.deadline == deadline)
        return query.all()
