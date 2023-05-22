from jose import jwt
from decouple import config


SECRET_KEY = config('SECRET_KEY_1') 
ALGORITHM = 'HS256'



def encode_token(token: dict) -> str:
    return jwt.encode(token, SECRET_KEY, algorithm=ALGORITHM)

async def decode_token(token: str) -> int:
    # try:
    token_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return await token_payload.get('sub')
    # except jwt.ExpiredSignatureError:
    #     raise UnauthorizedException (
    #         'EXPIRED_TOKEN',
    #         'Esse token está expirado.'
    #     )
    # except jwt.InvalidTokenError:
    #     raise UnauthorizedException (
    #         'INVALID_TOKEN',
    #         'Esse token é invalido.'
    #     )

