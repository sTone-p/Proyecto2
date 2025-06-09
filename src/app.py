from fastapi import FastAPI

from routes import api_router

api_server = FastAPI(
    description=('Proyecto Gestor de Ingresos y Salidas del curso Python+FastApi'),
    version='0.0.0',
    title= 'Gestor Ingresos y Salidas'
)

api_server.include_router(api_router)