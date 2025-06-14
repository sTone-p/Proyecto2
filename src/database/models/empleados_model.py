from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Integer, Float, ForeignKey
from src.database.models.base_model import BaseModel

class EmpleadosModel(BaseModel):
    __tablename__ = 'empleados'

    cantidad: Mapped[float] = mapped_column(Float(precision=2), default=0.0)
    vencimiento: Mapped[date] = mapped_column(Date())
    dia_de_pago: Mapped[date] = mapped_column(Date())
    status: Mapped[str] = mapped_column(String(20), default='pendiente')
    notas: Mapped[str] = mapped_column(String(2000))

    # Foreign key
    sueldo_empleados_id: Mapped[int] = mapped_column(Integer(), ForeignKey('empleados.id'))


