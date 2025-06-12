import asyncio 
from schemas.distribuidores_schemas import NewDistribuidoresRequest, UpdateDistribuidoresRequest, DistribuidoresResponses, DistribuidoresPaginatedResponse
from typing import List
from exceptions import app_exceptions as ae 

class DistribuidorService():
    def __init__(self, distribuidor_repo):
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
        from datetime import datetime
        return DistribuidoresResponses(
            id= 1,
            name= data.name,
            description= data.description,
            periodo_en_meses= data.periodo_en_meses,
            ultimo_dia_para_pagar= data.ultimo_pago_realizado,
            proximo_dia_a_pagar= data.próximo_dia_a_pagar,
            dia_estimado_a_pagar= data.dia_estimado_a_pagar,
            pagos= [],
            pagos_pendientes= False,
            created_at= datetime.now(),
            update_at= datetime.now(),
        )
    
    async def get_by_id(self, distribuidor_id: int) -> DistribuidoresResponses:
        raise ae.NotFoundError(f'El distribuidor #{distribuidor_id} no existe')

    async def update(self, distribuidor_id: int, data: UpdateDistribuidoresRequest) -> DistribuidoresResponses:
        raise ae.NotFoundError(f'El distribuidor #{distribuidor_id} no existe')

    async def delete(self, distribuidor_id: int) -> None:
        raise ae.NotFoundError(f'El distribuidor #{distribuidor_id} no existe')

    async def __count(self) -> int:
        return 0
    
    async def __get_distribuidores_list(self, page: int, limit: int) -> List[DistribuidoresResponses]:
        return []