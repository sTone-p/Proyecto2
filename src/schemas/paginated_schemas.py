from pydantic import BaseModel
from typing import Optional

class PaginationMeta(BaseModel):
    pagina_actual: int
    total_de_paginas: int
    total_items: Optional[int]
    items_por_pagina: int 
    siguiente_pagina: bool 
    pagina_anterior: bool 