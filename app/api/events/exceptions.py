from fastapi import status, HTTPException


class WrongEventId(HTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "No such event"
