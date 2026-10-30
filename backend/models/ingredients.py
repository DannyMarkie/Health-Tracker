from decimal import Decimal

from sqlalchemy import CheckConstraint, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    ingredient_id: Mapped[int] = mapped_column(primary_key=True)
    ingredient_brand: Mapped[str] = mapped_column(String(255))
    ingredient_name: Mapped[str] = mapped_column(String(255))
    ingredient_unit_id: Mapped[int] = mapped_column(ForeignKey("units.unit_id"))
    reference_amount: Mapped[int] = mapped_column(
        CheckConstraint("reference_amount>0", name="reference_amount_gt0")
    )
    energy_kcal: Mapped[int | None] = mapped_column(
        CheckConstraint("energy_kcal>=0", name="energy_kcal_gte0")
    )
    protein_g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2), CheckConstraint("protein_g>=0", name="ingredient_protein_gte0")
    )
    fat_g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2), CheckConstraint("fat_g>=0", name="ingredient_fat_gte0")
    )
    carb_g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2), CheckConstraint("carb_g>=0", name="ingredient_carb_gte0")
    )
    fibre_g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2), CheckConstraint("fibre_g>=0", name="ingredient_fibre_gte0")
    )
    package_amount: Mapped[int] = mapped_column(
        CheckConstraint("package_amount>0", name="package_amount_gt0")
    )
    package_price: Mapped[Decimal] = mapped_column(
        Numeric(7, 2), CheckConstraint("package_price>=0", name="ingredient_price_gte0")
    )
