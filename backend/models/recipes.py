from sqlalchemy import CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Recipe(Base):
    __tablename__ = "recipes"

    recipe_id: Mapped[int] = mapped_column(primary_key=True)
    recipe_name: Mapped[str] = mapped_column(String(255))
    servings: Mapped[int] = mapped_column(
        CheckConstraint("servings>0", name="servings_gt0")
    )
