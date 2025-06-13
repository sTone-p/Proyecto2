import asyncio 
import logging
from src.schemas.distribuidores_schemas import NewDistribuidoresRequest, UpdateDistribuidoresRequest, DistribuidoresResponses, DistribuidoresPaginatedResponse
from typing import List
from src.exceptions import app_exceptions as ae 
from src.repositories.distribuidor_repository import DistribuidorRepository

logger = logging.getLogger(__name__)

class DistribuidorService():
    def __init__(self, distribuidor_repo: DistribuidorRepository = DistribuidorRepository):
        self.distribuidor_repo = distribuidor_repo

    # CRUD
    async def get_paginated(self, page: int, limit: int) -> DistribuidoresPaginatedResponse:
        distribuidores, total_count = await asyncio.gather(
            self.__get_distribuidores_list(page, limit),
            self.__count(),
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Página {page} no existe')
        
        return DistribuidoresPaginatedResponse(
            results=distribuidores,
            paginacion={
                'pagina_actual': page,
                'total_de_paginas': total_pages,
                'total_items': total_count,
                'items_por_pagina': limit,
                'siguiente_pagina': page < total_pages,
                'pagina_anterior': page > 1,
            }
        )
    
    async def create(self, data: NewDistribuidoresRequest) -> DistribuidoresResponses:
        logger.debug(f'Creando Distribuidor: {data}')
        new_distribuidor = await self.distribuidor_repo.create(data.model_dump(mode='json'))
        logger.debug(f'Distribuidor creado {new_distribuidor}')
        return DistribuidoresResponses.model_validate(new_distribuidor)
    
    async def get_by_id(self, distribuidor_id: int) -> DistribuidoresResponses:
        logger.debug(f'Obteniendo Distribuidor por ID: {distribuidor_id}')
        distribuidor = await self.distribuidor_repo.get_one_by_criteria({'id': distribuidor_id})
        if distribuidor is None:
            raise ae.NotFoundError(f'El distribuidor #{distribuidor_id} no existe')
        return DistribuidoresResponses.model_validate(distribuidor)

    async def update(self, distribuidor_id: int, data: UpdateDistribuidoresRequest) -> DistribuidoresResponses:
        logger.debug(f'Actualizando distribuidor: {distribuidor_id} con datos {data}')
        distribuidor = await self.distribuidor_repo.update_one({'id': distribuidor_id}, data.model_dump(mode='json', exclude_unset=True))
        if distribuidor is None:
            raise ae.NotFoundError(f'El distribuidor #{distribuidor_id} no existe')
        return DistribuidoresResponses.model_validate(distribuidor)

    async def delete(self, distribuidor_id: int) -> None:
        logger.debug(f'Eliminando distribuidor: {distribuidor_id}')
        deleted = await self.distribuidor_repo.delete_one({'id': distribuidor_id})
        if not deleted:
            raise ae.NotFoundError(f'El distribuidor #{distribuidor_id} no existe')
        return None

    async def __count(self) -> int:
        return await self.distribuidor_repo.count()
    
    async def __get_distribuidores_list(self, page: int, limit: int) -> List[DistribuidoresResponses]:
        return await self.distribuidor_repo.get_many(page, limit)