from decimal import Decimal
from typing import Union

from pydantic import BaseModel
from sqlalchemy import CheckConstraint, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Ingredient(Base):
    __tablename__ = "ingredients"
    __table_args__ = (
        CheckConstraint("reference_amount>0", name="reference_amount_gt0"),
        CheckConstraint("protein_g>=0", name="ingredient_protein_gte0"),
        CheckConstraint("fat_g>=0", name="ingredient_fat_gte0"),
        CheckConstraint("carb_g>=0", name="ingredient_carb_gte0"),
        CheckConstraint("fibre_g>=0", name="ingredient_fibre_gte0"),
        CheckConstraint("package_amount>0", name="package_amount_gt0"),
        CheckConstraint("package_price>=0", name="ingredient_price_gte0"),
        CheckConstraint("energy_kcal>=0", name="energy_kcal_gte0"),
    )

    ingredient_id: Mapped[int] = mapped_column(primary_key=True)
    ingredient_brand: Mapped[str] = mapped_column(String(255))
    ingredient_name: Mapped[str] = mapped_column(String(255))
    ingredient_unit_id: Mapped[int] = mapped_column(ForeignKey("units.unit_id"))
    reference_amount: Mapped[int]
    energy_kcal: Mapped[int | None]
    protein_g: Mapped[Decimal | None] = mapped_column(Numeric(7, 2))
    fat_g: Mapped[Decimal | None] = mapped_column(Numeric(7, 2))
    carb_g: Mapped[Decimal | None] = mapped_column(Numeric(7, 2))
    fibre_g: Mapped[Decimal | None] = mapped_column(Numeric(7, 2))
    package_amount: Mapped[int]
    package_price: Mapped[Decimal] = mapped_column(Numeric(7, 2))

class IngredientsModel(BaseModel):
    ingredient_brand: str
    ingredient_name: str
    ingredient_unit_id: int
    reference_amount: int
    package_amount: int
    package_price: float
    energy_kcal: Union[int, None]
    protein_g: Union[float, None]
    fat_g: Union[float, None]
    carb_g: Union[float, None]
    fibre_g: Union[float, None]
