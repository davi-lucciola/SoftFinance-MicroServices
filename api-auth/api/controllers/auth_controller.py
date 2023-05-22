from http import HTTPStatus
from fastapi import Security, APIRouter, Depends, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..domain.services import auth_service
from ..domain.security import decode_token
from ..domain.models import Token, UserLogin


security_bearer = HTTPBearer()

async def authenticate(
        auth: HTTPAuthorizationCredentials = Security(security_bearer)) -> int:
    return await decode_token(auth.credentials)


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.get('/', status_code=HTTPStatus.OK)
async def get_auth(user_id: int = Depends(authenticate)) -> Response:
    return {
        'user_id': user_id
    }

@router.post('/login', status_code=HTTPStatus.OK)
async def login(user_login: UserLogin):
    token: Token = await auth_service.login()
    pass