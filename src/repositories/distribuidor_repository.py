from typing import List, Dict, Any

from base_repository import BaseRepository
from helpers.file_helpers import read_json_file, write_json_file
from config import app_settings
from database.models import DistribuidoresModel


class DistribuidorRepository(BaseRepository):
    def __init__(self, Model):
        super().__init__(DistribuidoresModel)

    #async def _read_all(self) -> List[Dict[str, Any]]:
    #    data = read_json_file(app_settings.PATH_DATA)
    #    return data.get('distribuidores', [])

    #async def _update_db(self, db: List[Dict[str, Any]]) -> None:
    #    current = read_json_file(app_settings.PATH_DATA)
    #    current['distribuidores'] = db
    #    write_json_file(app_settings.PATH_DATA, current)

    #async def _get_next_id(self) -> int:
    #    data = await self._read_all()
    #    if not data: 
    #        return 1
    #    return max(distribuidor['id'] for distribuidor in data) + 1
    
