from http import HTTPStatus
from fastapi import HTTPException
from ..models import UserIn, User
from ...infrastructure.repositories import user_repository


# Main flow
async def create_user(user: UserIn) -> None:
    validate_user(user)
    user: User = User(**user.dict(exclude={'confirm_password'}))
    user.hash_password()
    user_repository.create_user(user)

async def edit_user(id: int, user: UserIn, logged_user_id: int) -> None:
    resource_owner(id, logged_user_id)
    validate_user(user)
    user_exists(id)
    user: User = User(
        **user.dict(exclude={'confirm_password'}).update({'id': id})
    )
    user_repository.create_user(user)

async def delete_user(id: int, logged_user_id: int) -> None:
    resource_owner(id, logged_user_id)
    user_to_delete: User = user_exists(id)
    user_repository.delete_user(user_to_delete)

# Validations
def resource_owner(id: int, logged_user_id: int) -> None:
    if id != logged_user_id:
        raise HTTPException(
            status_code = HTTPStatus.UNAUTHORIZED,
            detail = 'Invalid resource owner, you can\'t do this.'
        )

def validate_user(user: UserIn) -> HTTPException | None:
    if len(user.password) < 8:
        raise HTTPException (
            status_code = HTTPStatus.BAD_REQUEST,
            detail='Password must contain at least eight characters.'
        )

    if not user.passwords_match():
        raise HTTPException (
            status_code = HTTPStatus.BAD_REQUEST,
            detail='Passwords must match.'
        )
    
    if user_repository.find_by_email(user.email) is not None:
        raise HTTPException (
            status_code = HTTPStatus.BAD_REQUEST,
            detail='That email is already registered.'
        )

def user_exists(id: int) -> HTTPException | User:
    user: list[User] = user_repository.find_by_id(id)

    if user is None:
        raise HTTPException (
            status_code = HTTPStatus.NOT_FOUND,
            detail='This user does not exists.'
        )
    
    return user[0]
