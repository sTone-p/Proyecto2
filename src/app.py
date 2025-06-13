from contextlib import asynccontextmanager

from fastapi import FastAPI
from routes import api_router
from .config.logger import configure_logging
from database import db_connection, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    if db_connection.connect():
        create_tables()
    yield
    db_connection.disconnect()
    
api_server = FastAPI(
    description='Proyecto Gestor de Ingresos y Salidas del curso Python+FastApi',
    version='0.0.0',
    title='Gestor Ingresos y Salidas',
    lifespan=lifespan,
)  

api_server.include_router(api_router)
