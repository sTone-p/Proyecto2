import logging

from src.schemas.empleados_schemas import NewEmpleadoRequest, UpdateEmpleadoRequest, EmpleadoResponse, EmpleadosPaginatedResponse
from src.exceptions.server_exceptions import InternalServerError, NotImplemented
from src.exceptions.client_exceptions import NotFound
from src.exceptions import app_exceptions as ae
from src.exceptions.base_http_exception import BaseHTTPException
from src.services.empleados_service import EmpleadoService

logger = logging.getLogger(__name__)

class EmpleadoController():
    def __init__(self, empleado_service: EmpleadoService):
        self.empleado_service = empleado_service

    async def get_paginated(self, page: int, limit: int) -> EmpleadosPaginatedResponse:
        try:
            empleados = await self.empleado_service.get_paginated(page, limit)
            return logger.debug(f'Encontrados {len(empleados)} Empleados')
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='EMPLEADO_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'EMPLEADO_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical('Error no contemplado en get_paginated')
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
           logger.critical('Error no contemplado en get_create')
           raise InternalServerError(
                message=f'Error al crear el empleado "{data.name}"',
                exception_code= 'EMPLEADO_UNHANDLED_ERROR'
                )
        
    async def get_by_id(self, empleado_id: int) -> EmpleadoResponse:
        try:
             return await self.empleado_service.get_by_id(empleado_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='EMPLEADO_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            logger.error(f'Empleado #{empleado_id} no encontrado en update_empleado')
            raise NotFound(ex.message, 'EMPLEADO_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical('Error no contemplado en get_by_id')
            raise InternalServerError(
                message=f'Error al obtener el empleado por ID #{empleado_id}',
                exception_code='EMPLEADO_UNHANDLED_ERROR'
            )

    async def update(self, empleado_id: int, data: UpdateEmpleadoRequest) -> EmpleadoResponse:
        try:
             return await self.empleado_service.update(empleado_id, data)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='EMPLEADO_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            logger.error(f'Empleado #{empleado_id} no encontrado en update_empleado')
            raise NotFound(ex.message, 'EMPLEADO_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical('Error no contemplado en get_update')
            raise InternalServerError(
                message=f'Error al actualizar el empleado #{empleado_id}',
                exception_code='EMPLEADO_UNHANDLED_ERROR'
            )

    async def delete(self, empleado_id: int) -> None:
        try:
             return await self.empleado_service.delete(empleado_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='EMPLEADO_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            logger.error(f'Empleado #{empleado_id} no encontrado en update_empleado')
            raise NotFound(ex.message, 'EMPLEADO_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical('Error no contemplado en get_delete')
            raise InternalServerError(
                message=f'Error al eliminar el empleado #{empleado_id}',
                exception_code='EMPLEADO_UNHANDLED_ERROR'
            )