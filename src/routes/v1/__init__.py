from fastapi import APIRouter

from .distribuidores_routes import router as distribuidores_router
from .empleados_routes import router as pago_a_empleados_router

router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(distribuidores_router, tags=['Distribuidores'])
router_v1.include_router(pago_a_empleados_router, tags=['Pago a Empleados'])