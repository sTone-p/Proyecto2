from schemas.empleados_schemas import NewEmpleadoRequest, UpdateEmpleadoRequest, EmpleadoResponse, EmpleadosPaginatedResponse
from exceptions.server_exceptions import InternalServerError, NotImplemented
from exceptions.client_exceptions import NotFound
from exceptions import app_exceptions as ae
from exceptions.base_http_exception import BaseHTTPException
from services.empleados_service import EmpleadoService

class EmpleadoController():
    def __init__(self, empleado_service: EmpleadoService):
        self.empleado_service = empleado_service

    async def get_paginated(self, page: int, limit: int) -> EmpleadosPaginatedResponse:
        try:
            return await self.empleado_service.get_paginated(page, limit)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='EMPLEADO_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'EMPLEADO_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al listar empleados',
                exception_code= 'EMPLEADO_UNHANDLED_ERROR'
                )
        
    async def create(self, data: NewEmpleadoRequest) -> EmpleadoResponse:
        try:
            return await self.empleado_service.create(data)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='EMPLEADO_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
           raise InternalServerError(
                message=f'Error al crear el empleado "{data.name}"',
                exception_code= 'EMPLEADO_UNHANDLED_ERROR'
                )
        
    async def get_by_id(self, empleado_id: int) -> EmpleadoResponse:
        try:
             return await self.empleado_service.get_by_id(empleado_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='EMPLEADO_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'EMPLEADO_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al obtener el empleado por ID #{empleado_id}',
                exception_code='EMPLEADO_UNHANDLED_ERROR'
            )

    async def update(self, empleado_id: int, data: UpdateEmpleadoRequest) -> EmpleadoResponse:
        try:
             return await self.empleado_service.update(empleado_id, data)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='EMPLEADO_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'EMPLEADO_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al actualizar el empleado #{empleado_id}',
                exception_code='EMPLEADO_UNHANDLED_ERROR'
            )

    async def delete(self, empleado_id: int) -> None:
        try:
             return await self.empleado_service.delete(empleado_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='EMPLEADO_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'EMPLEADO_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al eliminar el empleado #{empleado_id}',
                exception_code='EMPLEADO_UNHANDLED_ERROR'
            )