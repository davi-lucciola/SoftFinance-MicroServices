from http import HTTPStatus
from fastapi import APIRouter, Depends, Response
from .interceptors import authenticate
from ..domain.services import auth_service
from ..domain.models import UserLogin, Token


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.get('/', status_code=HTTPStatus.OK)
async def get_auth(user_id: int = Depends(authenticate)) -> Response:
    return {
        'user_id': user_id
    }

@router.post('/login', status_code=HTTPStatus.OK)
async def login(user_login: UserLogin) -> Response:
    token: Token = await auth_service.login()
    return {
        'acess_token': token.acess_token,
        'token_type' : 'Bearer',
        'user_id': token.user_id
    }