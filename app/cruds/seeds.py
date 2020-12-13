import sys
import pathlib
from datetime import datetime

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../../' )

from app.database import BASE, ENGINE, session_scope
from app.models.todos import Todo
from app.models.users import User

def generate_seed_data():
    BASE.metadata.create_all(ENGINE)
    users = [["太郎"], ["次郎"], ["花子"]]
    todos = [
        [1, "title1", "description1", datetime.now()],
        [1, "title2", "description2", datetime.now()],
        [2, "title3", "description3", datetime.now()],
        [2, "title4", "description4", datetime.now()],
        [3, "title5", "description5", datetime.now()],
        [3, "title6", "description6", datetime.now()]
    ]

    with session_scope() as session:
        for user in users:
            session.add(User(user[0]))
        for todo in todos:
            session.add(Todo(
                user_id = todo[0],
                title = todo[1],
                description = todo[2],
                deadline = todo[3]
            ))

if __name__ == "__main__":
    generate_seed_data()
