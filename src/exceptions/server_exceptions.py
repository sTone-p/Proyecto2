from fastapi import status

from .base_http_exception import BaseHTTPException


class InternalServerError(BaseHTTPException):
    description = 'UnhandledError',
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
    exception_code = 'API_UNHANDLED_ERROR'


class NotImplemented(BaseHTTPException):
    description = 'Service not implemented yet',
    status_code = status.HTTP_501_NOT_IMPLEMENTED,
    exception_code = 'API_ENDPOINT_NOT_IMPLEMENTED'