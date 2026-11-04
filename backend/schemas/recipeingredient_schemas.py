from decimal import Decimal

from pydantic import BaseModel, Field


class RecipeIngredientBase(BaseModel):
    recipe_id: int
    ingredient_id: int
    quantity: Decimal = Field(ge=0, max_digits=7, decimal_places=2)


class RecipeIngredientCreate(RecipeIngredientBase):
    pass

class RecipeIngredientRead(RecipeIngredientBase):
    pass

class RecipeIngredientUpdate(RecipeIngredientBase):
    pass
