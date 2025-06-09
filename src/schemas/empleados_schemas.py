from typing import Optional, List

from datetime import date, datetime

from pydantic import BaseModel, Field

from .paginated_schemas import PaginationMeta

class NewEmpleadoRequest(BaseModel):
    sueldo_empleados_id: int = Field(...,ge=1)
    cantidad: float = Field(...,gt=0)
    vencimiento: Optional[date] = None
    dia_de_pago: Optional[date] = None
    notas: Optional[str] = Field('', max_length=500)


class UpdateEmpleadoRequest(BaseModel):
    sueldo_empleados_id: Optional[int] = Field(None, ge=1)
    cantidad: Optional[float] = Field(None, gt=0)
    vencimiento: Optional[date] = None
    dia_de_pago: Optional[date] = None
    notas: Optional[str] = Field(None, max_length=500)


class EmpleadoResponse(BaseModel):
    id: int
    sueldo_empleados_id: int
    cantidad: float
    vencimiento: date
    dia_de_pago: date
    estado: str
    notas: str
    created_at: datetime
    updated_at: datetime



class EmpleadosPaginatedResponse(BaseModel):
    results: List[EmpleadoResponse]
    paginacion: PaginationMeta