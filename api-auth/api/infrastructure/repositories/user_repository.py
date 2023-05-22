from sqlmodel import select
from ..connection.session import commit_on_db, session_factory
from ...domain.models import User


def create_user(user: User) -> User:
    return commit_on_db(user)

def find_by_id(user_id: int) -> list[User] | None:
    with session_factory() as session:
        user: list[User] = session.execute (
            select(User).where(User.id == user_id)
        ).all()
        return user if len(user) > 0 else None

def find_by_email(email: str) -> list[User] | None:
    with session_factory() as session:
        result: list[User] = session.execute (
            select(User).where(User.email == email)
        ).all()
        return result if len(result) > 0 else None

def delete_user(user: User) -> None:
    with session_factory() as session:
        session.delete(user)
        session.commit()