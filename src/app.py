from contextlib import asynccontextmanager

from fastapi import FastAPI
from src.routes import api_router
from .config.logger import configure_logging
from src.database import db_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    db_connection.connect()
    yield
    db_connection.disconnect()
    
api_server = FastAPI(
    description='Proyecto Gestor de Ingresos y Salidas del curso Python+FastApi',
    version='0.0.0',
    title='Gestor Ingresos y Salidas',
    lifespan=lifespan,
)  

api_server.include_router(api_router)
