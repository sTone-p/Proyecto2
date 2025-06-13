import logging

from src.schemas.distribuidores_schemas import NewDistribuidoresRequest, UpdateDistribuidoresRequest, DistribuidoresResponses, DistribuidoresPaginatedResponse
from src.exceptions.server_exceptions import InternalServerError
from src.exceptions.client_exceptions import NotFound
from src.exceptions import app_exceptions as ae
from src.exceptions.base_http_exception import BaseHTTPException
from src.services.distribuidores_service import DistribuidorService

logger = logging.getLogger(__name__)


class DistribuidorController():
    def __init__(self, distribuidor_service: DistribuidorService):
        self.distribuidor_service = distribuidor_service

    async def get_paginated(self, page: int, limit: int) -> DistribuidoresPaginatedResponse:
        try:
            distribuidores = await self.distribuidor_service.get_paginated(page, limit)
            logger.debug(f'Encontrados {len(distribuidores)} Distribuidores')
            return distribuidores
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='DISTRIBUIDOR_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'DISTRIBUIDOR_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:    
            raise ex
        except Exception as ex:
            logger.critical('Error no contemplado en get_paginated')
            raise InternalServerError(
                message=f'Error al Listar Distribuidores',
                exception_code= 'DISTRIBUIDOR_UNHANDLED_ERROR'
                )

    async def create(self, data: NewDistribuidoresRequest) -> DistribuidoresResponses:
        try:
            return await self.distribuidor_service.create(data)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='DISTRIBUIDOR_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
           logger.critical('Error no contemplado en create')
           raise InternalServerError(
                message=f'Error al crear el Distribuidor "{data.name}"',
                exception_code= 'DISTRIBUIDOR_UNHANDLED_ERROR'
                )
        
    async def get_by_id(self, distribuidor_id: int) -> DistribuidoresResponses:
        try:
            return await self.distribuidor_service.get_by_id(distribuidor_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='DISTRIBUIDOR_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            logger.error(f'Distribuidor #{distribuidor_id} no encontrado en distribuidor get_by_id')
            raise NotFound(ex.message, 'DISTRIBUIDOR_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical('Error no contemplado en get_by_id')
            raise InternalServerError(
                message=f'Error al obtener distribuidor por ID #{distribuidor_id}',
                exception_code= 'DISTRIBUIDOR_UNHANDLED_ERROR'
                )

    async def update(self, distribuidor_id: int, data: UpdateDistribuidoresRequest) -> DistribuidoresResponses:
        try:
            return await self.distribuidor_service.update(distribuidor_id, data)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='DISTRIBUIDOR_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            logger.error(f'Distribuidor #{distribuidor_id} no encontrado en update_distribuidor')
            raise NotFound(ex.message, 'DISTRIBUIDOR_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical('Error no contemplado en update')
            raise InternalServerError(
                message=f'Error al actualizar el distribuidor por ID #{distribuidor_id}',
                exception_code= 'DISTRIBUIDOR_UNHANDLED_ERROR'
                )

    async def delete(self, distribuidor_id: int) -> None:
        try:
            return await self.distribuidor_service.delete(distribuidor_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='DISTRIBUIDOR_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            logger.error(f'Distribuidor #{distribuidor_id} no encontrado en delete_distribuidor')
            raise NotFound(ex.message, 'DISTRIBUIDOR_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical('Error no contemplado en delete')
            raise InternalServerError(
                message=f'Error al eliminar distribuidor por ID #{distribuidor_id}',
                exception_code= 'DISTRIBUIDOR_UNHANDLED_ERROR'
            )

