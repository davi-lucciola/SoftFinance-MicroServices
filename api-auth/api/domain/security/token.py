from jose import jwt, exceptions
from decouple import config
from http import HTTPStatus
from fastapi import HTTPException


SECRET_KEY: str = config('SECRET_KEY_1') 
ALGORITHM = 'HS256'


def encode_token(token: dict) -> str:
    return jwt.encode(token, SECRET_KEY, algorithm=ALGORITHM)

async def decode_token(token: str) -> int:
    try:
        token_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return token_payload['sub']
    except exceptions.ExpiredSignatureError as e:
        raise HTTPException (
                detail = 'Token has expired.',
                status_code = HTTPStatus.UNAUTHORIZED
        ) from exc
    except exceptions.JWTClaimsError as e:
        raise HTTPException (
            detail = 'Invalid Token.',
            status_code = HTTPStatus.UNAUTHORIZED
        ) from exc

