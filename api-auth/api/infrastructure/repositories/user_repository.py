from sqlmodel import select
from ..connection.session import commit_on_db, session_factory
from ...domain.models import User


def create_user(user: User) -> User:
    return commit_on_db(user)

def find_by_id(id: int) -> User | None:
    with session_factory() as session:
        user: User = session.exec(select(User).where(User.id == id))
        return user[0] if len(user) != 0 else None

def delete_user(user: User) -> None:
    with session_factory() as session:
        session.delete(user)
        session.commit()