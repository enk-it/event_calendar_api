from fastapi import status, HTTPException

from api.exceptions import BaseHTTPException


class WrongEventId(BaseHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "No such event"
