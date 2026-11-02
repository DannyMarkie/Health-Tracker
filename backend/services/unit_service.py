from models.unit import Unit
from sqlalchemy.orm import Session


class UnitService:
    def __init__(self, session: Session) -> None:
        self._db = session

    def list_units(self) -> list[Unit]:
        return self._db.query(Unit).all()
