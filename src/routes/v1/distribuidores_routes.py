from typing import Annotated

from fastapi import APIRouter, Path, Query

from schemas.distribuidores_schemas import NewDistribuidoresRequest, UpdateDistribuidoresRequest, DistribuidoresResponses, DistribuidoresPaginatedResponse

router = APIRouter(
    prefix='/Distribuidores',
    responses={
        400: {'description': 'Bad Request. Revisa la info del body y/o parámetros.'},
        401: {'description': 'Unauthorized. Credenciales inválidas o no enviadas.'},
        403: {'description': 'Forbidden. No tienes acceso a este recurso.'},
        500: {'description': 'Internal Server Error. Error de servidor, contacta al sysadmin.'},
        501: {'description': 'Not implemented. Función aún no implementada.'},
    }
)


@router.get(
    '',
    name='Distribuidores',
    description= 'Lista de Distribuidores',
    response_description='Retorna una lista de Distribuidores',
    status_code=200,
    responses={
        400: {'description': 'Bad Request. Revisa los parámetros de paginación o filtrado.'}
    }
)
async def get_paginated(
    page: Annotated[int, Query(ge=1)] = 1,
      limit: Annotated[int, Query(ge=1, le=100)] = 10,
      ) -> DistribuidoresPaginatedResponse:
    # TODO: Implementar paginación
    # TODO: Implementar filtros
    # TODO: Implementar tiempo de respuesta
    return {
        'results': [
            {        
                'id': 1,
                'name': 'Factura',
                'description': 'Factura Distribuidor.',
                'periodo_en_meses': 1,
                'ultimo_dia_para_pagar': "2025-06-07",
                'proximo_dia_a_pagar': None,
                'dia_estimado_a_pagar': "2025-07-01",
                'pagos': [],
                'pagos_pendientes': False,
                'created_at': '2025-07-18T02:18:27Z',
                'update_at': '2025-07-18T02:18:27Z',
            }
        ],
        'paginacion': {
            'pagina_actual': page,
            'total_de_paginas': 5,
            'total_items': 1,
            'items_por_pagina': limit,
            'siguiente_pagina': False,
            'pagina_anterior': False,
        }
    }
   


@router.post(
        '',
        name='Añadir Distribuidor',
        status_code=201,
        responses={
            201: {'description': 'Añadido nuevo distribuidor'},
            400: {'descrpition': 'Revisa el body request'},
        }
)
async def create(new_distribuidor: NewDistribuidoresRequest) -> DistribuidoresResponses:
    return {
        'id': 1,
        'name': 'Factura',
        'description': 'Factura Distribuidor.',
        'periodo_en_meses': 1,
        'ultimo_dia_para_pagar': "2025-07-01",
        'proximo_dia_a_pagar': None,
        'dia_estimado_a_pagar': "2025-07-01",
        'pagos': [],
        'pagos_pendientes': False,
        'created_at': '2025-07-18T02:18:27Z',
        'update_at': '2025-07-18T02:18:27Z',
    }


@router.get(
        '/{distribuidores_id}',
        name='Obtener gastos por ID',
        responses={
            200: {'description': 'Pago Encontrado'},
            404: {'description': 'Pago NO Encontrado'},
        }
)
async def get_by_id(distribuidores_id: Annotated [int, Path(ge=1, description= 'ID del distribuidor a buscar', title= 'ID del Distribuidor')]) -> DistribuidoresResponses:
    # TODO implementar busqueda por ID
    return {
        'id': distribuidores_id,
        'name': 'Factura',
        'description': 'Factura Distribuidor.',
        'periodo_en_meses': 1,
        'ultimo_dia_para_pagar': "2025-07-01",
        'proximo_dia_a_pagar': None,
        'dia_estimado_a_pagar': "2025-07-01",
        'pagos': [],
        'pagos_pendientes': False,
        'created_at': '2025-07-18T02:18:27Z',
        'update_at': '2025-07-18T02:18:27Z',
    }


@router.patch(
        '/{distribuidores_id}',
        name='Actualizar datos de pago a distribuidores',
        responses={
            200: {'description': 'Pago Actualizado'},
            404: {'description': 'Pago NO Encontrado'},
        }
)
async def update_by_id(
    distribuidores_id: Annotated [int, Path(ge=1, description= 'ID del distribuidor a Actualizar', title= 'ID del Distribuidor')], distribuidor_data: UpdateDistribuidoresRequest
) -> DistribuidoresResponses:
    # TODO Implementar Actualizacion por ID
    # Campos a recibir
    # - name: Optional
    # - description: Optional
    # - periodo en meses: Optional
    # - Ultimo dia para pagar: Optional 
    # - Próximo dia a pagar: Optional
    # - Dia estimado a pagar: Optional
    return {
        'id': distribuidores_id,
        'name': 'Factura',
        'description': 'Factura Distribuidor.',
        'periodo_en_meses': 1,
        'ultimo_dia_para_pagar': "2025-07-01",
        'proximo_dia_a_pagar': None,
        'dia_estimado_a_pagar': "2025-07-01",
        'pagos': [],
        'pagos_pendientes': False,
        'created_at': '2025-07-18T02:18:27Z',
        'update_at': '2025-07-18T02:18:27Z',
    }


@router.delete(
        '/{distribuidores_id}',
        name='Borrar pagos por ID',
        status_code= 204,
        responses={
            200: {'description': 'Pago borrado'},
            404: {'description': 'Pago NO Encontrado, no se borro'},
    }
)
async def delete_by_id(distribuidores_id: Annotated [int, Path(ge=1, description= 'ID del distribuidor a Eliminar', title= 'ID del Distribuidor')]):
    # TODO Implementar borrado por ID
    return None