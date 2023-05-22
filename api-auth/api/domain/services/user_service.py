from http import HTTPStatus
from fastapi import HTTPException
from ..models import UserIn, User
from ...infrastructure.repositories import user_repository


# Main flow
async def create_user(user: UserIn) -> int:
    validate_user(user)
    user: User = User(**user.dict(exclude={'confirm_password'}))
    user.hash_password()
    return user_repository.create_user(user).id

async def edit_user(id: int, user: UserIn) -> None:
    validate_user(user)
    user_exists(id)
    user: User = User(
        **user.dict(exclude={'confirm_password'}).update({'id': id})
    )
    user_repository.create_user(user)

async def delete_user(id: int) -> None:
    user_to_delete: User = user_exists(id)
    user_repository.delete_user(user_to_delete)

# Validations
def validate_user(user: UserIn) -> HTTPException | None:
    if len(user.password) < 8:
        return HTTPException (
            status_code = HTTPStatus.BAD_REQUEST,
            detail='Password must contain at least eight characters'
        )

    if not user.passwords_match():
        return HTTPException (
            status_code = HTTPStatus.BAD_REQUEST,
            detail='Passwords must match'
        )

def user_exists(id: int) -> HTTPException | User:
    user_in_db: User = user_repository.find_by_id(id)

    if user_in_db is None:
        return HTTPException (
            status_code = HTTPStatus.NOT_FOUND,
            detail='This user does not exists'
        )
    
    return user_in_db
