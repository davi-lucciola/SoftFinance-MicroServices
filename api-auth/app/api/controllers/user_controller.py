from http import HTTPStatus
from fastapi import APIRouter
from domain.models import UserIn, User
from domain.services import user_service


router = APIRouter()


@router.post('/users', status_code = HTTPStatus.OK)
async def create_user(user: UserIn) -> User:
    return await user_service.create_user(user)