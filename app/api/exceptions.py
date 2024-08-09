from fastapi import status
from fastapi.exceptions import HTTPException


class BaseHTTPException(HTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad Request"

    def __init__(self):
        super().__init__(
            status_code=self.status_code,
            detail=self.detail
        )
