from models.ingredients import Ingredient, IngredientsModel
from sqlalchemy.orm import Session


class IngredientService:
    def __init__(self, session: Session) -> None:
        self._db = session

    def list_ingredients(self) -> list[Ingredient]:
        return self._db.query(Ingredient).all()

    def add_ingredient(self, ingredient: IngredientsModel):
        db_ingredient = Ingredient(**ingredient.model_dump())
        self._db.add(db_ingredient)
        self._db.commit()
        self._db.refresh(db_ingredient)
        return db_ingredient
