from typing import List, Dict, Any

from base_repository import BaseRepository
from helpers.file_helpers import read_json_file, write_json_file
from config import app_settings


#class EmpleadoRepository(BaseRepository):
class EmpleadoRepository():
    async def _read_all(self) -> List[Dict[str, Any]]:
        data = read_json_file(app_settings.PATH_DATA)
        return data['empleados']

    async def _update_db(self, data: List[Dict[str, Any]]) -> None:
        db = read_json_file(app_settings.PATH_DATA)
        db['empleados'] = data
        write_json_file(app_settings.PATH_DATA, db)

    async def _get_next_id(self) -> int:
        data = await self._read_all()
        if not data: 
            return 1
        return max(empleados['id'] for empleados in data) + 1
    
