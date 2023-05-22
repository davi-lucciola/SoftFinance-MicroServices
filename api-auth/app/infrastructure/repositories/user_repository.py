from domain.models import User
from infrastructure.connection.session import commit_on_db


def create_user(user: User) -> User:
    return commit_on_db(user)