from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Unit(Base):
    __tablename__ = "units"

    unit_id: Mapped[int] = mapped_column(primary_key=True)
    unit_code: Mapped[str] = mapped_column(String(255), unique=True)
    unit_display_name: Mapped[str] = mapped_column(String(255))
