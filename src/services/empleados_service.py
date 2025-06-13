import asyncio 
import logging
from src.schemas.empleados_schemas import NewEmpleadoRequest, UpdateEmpleadoRequest, EmpleadoResponse, EmpleadosPaginatedResponse
from typing import List
from src.exceptions import app_exceptions as ae 
from src.repositories.empleado_repository import EmpleadoRepository

logger = logging.getLogger(__name__)

class EmpleadoService():
    def __init__(self, empleado_repo: EmpleadoRepository = EmpleadoRepository()):
        self.empleado_repo = empleado_repo

    # CRUD
    async def get_paginated(self, page: int, limit: int) -> EmpleadosPaginatedResponse:
        empleados, total_count = await asyncio.gather(
            self.__get_empleados_list(page, limit),
            self.__count(),
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Página {page} no existe')
        
        return EmpleadosPaginatedResponse(
            results=empleados,
            paginacion={
                'pagina_actual': page,
                'total_de_paginas': total_pages,
                'total_items': total_count,
                'items_por_pagina': limit,
                'siguiente_pagina': page < total_pages,
                'pagina_anterior': page > 1,
            }
        )
    
    async def create(self, data: NewEmpleadoRequest) -> EmpleadoResponse:
        logger.debug(f'Creando Empleado: {data}')
        new_empleado = await self.empleado_repo.create(data.model_dump(mode='json'))
        logger.debug(f'Empleado creado: {new_empleado}')
        return new_empleado
    
    async def get_by_id(self, empleado_id: int) -> EmpleadoResponse:
        logger.debug(f'Obteniendo empleado por ID: {empleado_id}')
        empleado = await self.empleado_repo.get_one_by_criteria({'id': empleado_id})
        if empleado is None:
            raise ae.NotFoundError(f'El empleado #{empleado_id} no existe')
        return EmpleadoResponse.model_validate(empleado)
    
    async def update(self, empleado_id: int, data: UpdateEmpleadoRequest) -> EmpleadoResponse:
        logger.debug(f'Actualizando empleado: {data}')
        empleado = await self.empleado_repo.update_one({'id': empleado_id}, data.model_dump(mode='json', exclude_unset=True))
        if empleado is None:
            raise ae.NotFoundError(f'El empleado #{empleado_id} no existe')

    async def delete(self, empleado_id: int) -> None:
        logger.debug(f'Eliminando empleado: {empleado_id}')
        deleted = await self.empleado_repo.delete_one({'id': empleado_id})
        if not deleted:
            raise ae.NotFoundError(f'El empleado #{empleado_id} no existe')

    async def __count(self) -> int:
        return await self.empleado_repo.count()
    
    async def __get_empleados_list(self, page: int, limit: int) -> List[EmpleadoResponse]:
        return await self.empleado_repo.get_many(page, limit)