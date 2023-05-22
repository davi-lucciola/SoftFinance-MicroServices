from fastapi import Security, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..domain.services import auth_service
from ..domain.models import Token
from ..domain.security import decode_token


security_bearer = HTTPBearer()

async def authenticate (
    auth: HTTPAuthorizationCredentials = Security(security_bearer)
) -> int:
    return await decode_token(auth.credentials)
   