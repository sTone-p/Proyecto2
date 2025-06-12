from schemas.distribuidores_schemas import NewDistribuidoresRequest, UpdateDistribuidoresRequest, DistribuidoresResponses, DistribuidoresPaginatedResponse
from exceptions.server_exceptions import InternalServerError, NotImplemented
from exceptions.client_exceptions import NotFound
from exceptions import app_exceptions as ae
from exceptions.base_http_exception import BaseHTTPException
from services.distribuidores_service import DistribuidorService


class DistribuidorController():
    def __init__(self, distribuidor_service: DistribuidorService):
        self.distribuidor_service = distribuidor_service

    async def get_paginated(self, page: int, limit: int) -> DistribuidoresPaginatedResponse:
        try:
            return await self.distribuidor_service.get_paginated(page, limit)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='DISTRIBUIDOR_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'DISTRIBUIDOR_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:    
            raise ex
        except Exception as ex:
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
           raise InternalServerError(
                message=f'Error al crear el Distribuidor "{data.name}"',
                exception_code= 'DISTRIBUIDOR_UNHANDLED_ERROR'
                )
        
    async def get_by_id(self, distribuidor_id: int) -> DistribuidoresResponses:
        try:
            return await self.distribuidor_service.get_by_id(distribuidor_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='DISTRIBUIDOR_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'DISTRIBUIDOR_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al obtener distribuidor por ID #{distribuidor_id}',
                exception_code= 'DISTRIBUIDOR_UNHANDLED_ERROR'
                )

    async def update(self, distribuidor_id: int, data: UpdateDistribuidoresRequest) -> DistribuidoresResponses:
        try:
            return await self.distribuidor_service.update(distribuidor_id, data)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='DISTRIBUIDOR_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'DISTRIBUIDOR_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al actualizar el distribuidor por ID #{distribuidor_id}',
                exception_code= 'DISTRIBUIDOR_UNHANDLED_ERROR'
                )

    async def delete(self, distribuidor_id: int) -> None:
        try:
            return await self.distribuidor_service.get_delete(distribuidor_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='DISTRIBUIDOR_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'DISTRIBUIDOR_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al eliminar distribuidor por ID #{distribuidor_id}',
                exception_code= 'DISTRIBUIDOR_UNHANDLED_ERROR'
            )

