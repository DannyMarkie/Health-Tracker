from fastapi import HTTPException, status
from models.ingredients import Ingredient
from schemas.ingredient_schemas import IngredientCreate, IngredientUpdate
from sqlalchemy.orm import Session


class IngredientService:
    def __init__(self, session: Session) -> None:
        self._db = session

    def list_ingredients(self) -> list[Ingredient]:
        return self._db.query(Ingredient).all()

    def add_ingredient(self, ingredient: IngredientCreate):
        db_ingredient = Ingredient(**ingredient.model_dump())
        self._db.add(db_ingredient)
        self._db.commit()
        self._db.refresh(db_ingredient)
        return db_ingredient

    def update_ingredient(self, ingredient_id: int, ingredient: IngredientUpdate):
        db_ingredient = (
            self._db.query(Ingredient)
            .filter(Ingredient.ingredient_id == ingredient_id)
            .first()
        )

        if db_ingredient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient not found"
            )

        for field, value in ingredient.model_dump(exclude_unset=True).items():
            setattr(db_ingredient, field, value)

        self._db.commit()
        self._db.refresh(db_ingredient)
        return db_ingredient

    def remove_ingredient(self, ingredient_id: int):
        db_ingredient = (
            self._db.query(Ingredient)
            .filter(Ingredient.ingredient_id == ingredient_id)
            .first()
        )

        if db_ingredient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient not found"
            )

        self._db.delete(db_ingredient)
        self._db.commit()
        return db_ingredient
