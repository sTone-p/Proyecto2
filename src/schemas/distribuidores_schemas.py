from typing import Optional, List   
from datetime import date, datetime

from pydantic import BaseModel, Field

from .paginated_schemas import PaginationMeta


class NewDistribuidoresRequest(BaseModel):
    name: str = Field(..., min_length=5, max_length=100)
    description: Optional[str] = Field('', max_length=500)
    periodo_en_meses: int = Field(..., ge=1, le=12)
    ultimo_pago_realizado: Optional[date] = None
    próximo_dia_a_pagar: Optional[date] = None
    dia_estimado_a_pagar: Optional[date] = None


class UpdateDistribuidoresRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=5, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    periodo_en_meses: Optional[int] = Field(None, ge=1, le=12)
    ultimo_pago_realizado: Optional[date] = None
    próximo_dia_a_pagar: Optional[date] = None
    dia_estimado_a_pagar: Optional[date] = None



class DistribuidoresResponses(BaseModel):
    id: int
    name: str
    description: str
    periodo_en_meses: int
    ultimo_dia_para_pagar: Optional[date]
    proximo_dia_a_pagar: Optional[date]
    dia_estimado_a_pagar: Optional[date]
    pagos: list = []
    pagos_pendientes: bool
    created_at: datetime
    update_at: datetime


class DistribuidoresPaginatedResponse(BaseModel):
    results: List[DistribuidoresResponses]
    paginacion: PaginationMeta