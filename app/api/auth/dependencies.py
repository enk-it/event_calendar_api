from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.auth.exceptions import TokenInvalid
from api.config import settings

http_bearer = HTTPBearer()


def get_token_payload(
        credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> str:
    token = credentials.credentials
    return token


async def get_current_auth_user(
        token_payload: str = Depends(get_token_payload),
) -> str:
    print("DEBUG")
    print(token_payload)
    print(settings.ADMIN_KEY)
    if token_payload != settings.ADMIN_KEY:
        raise TokenInvalid
    return "ok"
