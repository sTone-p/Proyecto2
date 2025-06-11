from typing import Annotated

from fastapi import APIRouter, Query, Path

from schemas.empleados_schemas import NewEmpleadoRequest, UpdateEmpleadoRequest, EmpleadoResponse, EmpleadosPaginatedResponse

from .dependencies import empleado_controller

router = APIRouter(
    prefix='/Pago Empleados',
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
    name='Lista pago empleados',
    description='Lista de pagos a empleados',
    responses={
        200: {'description': 'Lista de pagos paginada'},
        400: {'description': 'Bad Request. Revisa los parámetros de paginación o filtrado.'},        
    }
)
async def get_paginated(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
) -> EmpleadosPaginatedResponse:
    return await empleado_controller.get_paginated(page, limit)



@router.post(
        '',
        name='Crear nuevo pago',
        status_code=201,
        responses={
            201: {'description': 'Pago creado.'},
            400: {'description': 'Error. Verifique la info.'}
        }     
)
async def create(new_pago: NewEmpleadoRequest) -> EmpleadoResponse: 
    return await empleado_controller.get_by_id(new_pago)

@router.get(
        '/{pago_a_empleados_id}',
        name='Obtener pago por ID',
        responses={
            201: {'description': 'Pago encontrado.'},
            400: {'description': 'Pago NO encontrado.'}
        }  
)
async def get_by_id(pago_a_empleados_id: Annotated[int, Path(ge=1, title='ID del pago')]) -> EmpleadoResponse:
    return await empleado_controller.get_by_id(pago_a_empleados_id)


@router.patch(
        '/{pago_a_empleados_id}',
        name='Actualizar pago a empleados por ID',
        responses={
            200: {'description': 'Pago actualizado.'},
            400: {'description': 'Bad Request. Verifique la info'},
            400: {'description': 'Pago no encontrado.'}
        }
)
async def update_by_id(
    pago_a_empleados_id: Annotated[int, Path(title='ID del pago')],
    pago_data: UpdateEmpleadoRequest,
    ) -> EmpleadoResponse:
    return await empleado_controller.update_by_id(pago_a_empleados_id)


@router.delete(
        '/{pago_a_empleados_id}',
        name='Eliminar pago por ID',
        status_code= 204,
        responses={
            204: {'description': 'Pago eliminado.'},
            404: {'description': 'Pago NO encontrado.'}
        }
)
async def delete_by_id(pago_a_empleados_id: Annotated[int, Path(ge=1, title='ID del Pago')]) -> None:
    return await empleado_controller.get_by_id(pago_a_empleados_id)