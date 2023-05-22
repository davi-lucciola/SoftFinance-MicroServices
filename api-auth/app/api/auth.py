from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from domain.security import decode_token


security_bearer = HTTPBearer()

async def autenticar(
        auth: HTTPAuthorizationCredentials = Security(security_bearer)) -> int:
    return await decode_token(auth.credentials)