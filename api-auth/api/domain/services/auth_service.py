from http import HTTPStatus
from fastapi import HTTPException
from datetime import datetime as dt, timedelta
from ..security import encode_token
from ..models import Token, User, UserLogin
from ...infrastructure.repositories import user_repository, token_repository


async def login(user: UserLogin) -> Token:
    user_in_db: User = user_repository.find_by_field(User, 'email', user)

    if user_in_db is None or not user.passwords_match(user_in_db.password):
        return HTTPException (
            status_code = HTTPStatus.UNAUTHORIZED,
            detail='Email and/or password are incorect.'
        )
    
    return create_token(user_in_db.id)
    
def create_token(user_id: int) -> Token:
    EXPIRE_MINUTES = 10
    initiated_at: dt = dt.utcnow()
    expire_at: dt = dt.utcnow() + timedelta(minutes=EXPIRE_MINUTES)

    token: Token = Token (
        initiated_at=initiated_at, 
        expire_at=expire_at,
        user_id=user_id,
        acess_token=encode_token({
            'exp': expire_at,
            'iat': initiated_at,
            'sub': user_id
        })
    )

    token_in_db: Token = token_repository.get_token_by_user_id(user_id)
    
    if token is not None:
        token.id = token_in_db.id

    return token_repository.save_token(token)
    