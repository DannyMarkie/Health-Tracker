from decimal import Decimal

from sqlalchemy import CheckConstraint, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"
    __table_args__ = (CheckConstraint("quantity>0", name="quantity_gt0"),)

    recipe_id: Mapped[int] = mapped_column(
        ForeignKey("recipes.recipe_id", ondelete="CASCADE"), primary_key=True
    )
    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.ingredient_id"), primary_key=True
    )
    quantity: Mapped[Decimal] = mapped_column(Numeric(7, 2))
