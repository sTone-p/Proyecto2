from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Integer
from base_model import BaseModel

class DistribuidoresModel(BaseModel):
    __tablename__ = 'Distribuidores'

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    periodo_en_meses: Mapped[int] = mapped_column(Integer(), nullable=False)
    ultimo_pago_realizado: Mapped[date] = mapped_column(Date(), nullable=False)
    próximo_dia_a_pagar: Mapped[date] = mapped_column(Date(), nullable=False)
    dia_estimado_a_pagar: Mapped[date] = mapped_column(Date(), nullable=False)