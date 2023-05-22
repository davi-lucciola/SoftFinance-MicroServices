from http import HTTPStatus
from fastapi import APIRouter, Response, Depends
from .interceptors import authenticate
from ..domain.models import UserIn
from ..domain.services import user_service


router = APIRouter(prefix='/users',tags=['Users'])


@router.post('/', status_code = HTTPStatus.OK)
async def create_user(user: UserIn) -> Response:
    await user_service.create_user(user)
    return {
        'detail': 'User created sucessfully'
    }

@router.put('/{id}', status_code = HTTPStatus.OK)
async def edit_user (
    id: int, user: UserIn, user_id: int = Depends(authenticate)
) -> Response:
    await user_service.edit_user(id, user, user_id)
    return {
        'detail': 'User edited sucessfully'
    }

@router.delete('/{id}', status_code = HTTPStatus.OK)
async def delete_user(id: int, user_id: int = Depends(authenticate)) -> Response:
    await user_service.delete_user(id, user_id)
    return {
        'detail': 'User deleted sucessfully'
    }
