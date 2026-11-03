from models.recipes import Recipe
from schemas.recipe_schemas import RecipeCreate
from sqlalchemy.orm import Session


class RecipeService:
    def __init__(self, session: Session) -> None:
        self._db = session

    def list_recipes(self) -> list[Recipe]:
        return self._db.query(Recipe).all()

    def add_recipe(self, recipe: RecipeCreate):
        print(Recipe(**recipe.model_dump()))
        db_recipe = Recipe(**recipe.model_dump())
        self._db.add(db_recipe)
        self._db.commit()
        self._db.refresh(db_recipe)
        return db_recipe
