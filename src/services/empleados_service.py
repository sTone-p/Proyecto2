import asyncio 
from schemas.empleados_schemas import NewEmpleadoRequest, UpdateEmpleadoRequest, EmpleadoResponse, EmpleadosPaginatedResponse
from typing import List
from exceptions import app_exceptions as ae 


class EmpleadoService():
    def __init__(self, empleado_repo):
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
        from datetime import datetime
        return EmpleadoResponse(
            id= 1,
            sueldo_empleados_id= data.sueldo_empleados_id,
            cantidad= data.cantidad,
            vencimiento= data.vencimiento,
            dia_de_pago= data.dia_de_pago,
            estado= 'pendiente',
            notas= data.notas,
            created_at= datetime.now(),
            updated_at= datetime.now()
        )
    
    async def get_by_id(self, empleado_id: int) -> EmpleadoResponse:
        raise ae.NotFoundError(f'El empleado #{empleado_id} no existe')

    async def update(self, empleado_id: int, data: UpdateEmpleadoRequest) -> EmpleadoResponse:
        raise ae.NotFoundError(f'El empleado #{empleado_id} no existe')

    async def delete(self, empleado_id: int) -> None:
        raise ae.NotFoundError(f'El empleado #{empleado_id} no existe')

    async def __count(self) -> int:
        return 0
    
    async def __get_empleados_list(self, page: int, limit: int) -> List[EmpleadoResponse]:
        return []