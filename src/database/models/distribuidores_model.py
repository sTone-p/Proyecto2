from datetime import date
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Integer
from src.database.models.base_model import BaseModel
from src.database.models.empleados_model import EmpleadosModel

class DistribuidoresModel(BaseModel):
    __tablename__ = 'Distribuidores'

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    periodo_en_meses: Mapped[int] = mapped_column(Integer(), nullable=False)
    ultimo_pago_realizado: Mapped[date] = mapped_column(Date(), nullable=False)
    próximo_dia_a_pagar: Mapped[date] = mapped_column(Date(), nullable=False)
    dia_estimado_a_pagar: Mapped[date] = mapped_column(Date(), nullable=False)

    # Relationships
    empleados: Mapped[List[EmpleadosModel]] = relationship(EmpleadosModel)

    def to_dict(self) -> dict:
        response = super().to_dict()
        response['empleados'] = [empleado.to_dict() for empleado in self.empleados]
        return response