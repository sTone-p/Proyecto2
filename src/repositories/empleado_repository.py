from src.repositories.base_repository import BaseRepository
from src.database.models.empleados_model import EmpleadosModel

    
class EmpleadoRepository(BaseRepository):
    def __init__(self):
        super().__init__(EmpleadosModel)