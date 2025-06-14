from src.config import app_settings
from src.database.database_connection import DataBaseConnection
from src.database.models import BaseModel


db_connection = DataBaseConnection(app_settings.DB_CONN)


#def create_tables():
#    print('\033[94m', 'Crear tablas en la DB', '\033[0m')
#    BaseModel.metadata.create_all(bind=db_connection.engine)