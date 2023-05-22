from domain.models import UserIn, User
from infrastructure.repositories import user_repository


def create_user(user: UserIn) -> int:
    user: User = User(**user.dict(exclude={'confirm_password'}))
    return user_repository.create_user(user).id