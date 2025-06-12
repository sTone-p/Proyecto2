from typing import Optional

class BaseAppExtensions(Exception):
    default_message: str = 'UNKNOWN ERROR'

    def __init__(self, message: Optional[str] = None):
        self.message = message or self.default_message
        super().__init__(self.message)

class NotFoundError(BaseAppExtensions):
    default_message = 'Recurso no encontrado'