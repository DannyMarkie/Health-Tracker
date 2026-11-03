from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

NonNegDecimal = Annotated[Decimal, Field(ge=0, max_digits=7, decimal_places=2)]


class IngredientBase(BaseModel):
    ingredient_brand: str = Field(min_length=1, max_length=255)
    ingredient_name: str = Field(min_length=1, max_length=255)
    ingredient_unit_id: int
    reference_amount: int = Field(gt=0)
    package_amount: int = Field(gt=0)
    package_price: NonNegDecimal
    energy_kcal: int | None = Field(default=None, ge=0)
    protein_g: NonNegDecimal | None = None
    fat_g: NonNegDecimal | None = None
    carb_g: NonNegDecimal | None = None
    fibre_g: NonNegDecimal | None = None


class IngredientCreate(IngredientBase):
    pass


class IngredientRead(IngredientBase):
    model_config = ConfigDict(from_attributes=True)
    ingredient_id: int