from typing import Annotated

from database import Connection
from fastapi import APIRouter, Depends
from models.unit import Unit
from services.unit_service import UnitService

router = APIRouter()


def get_unit_service() -> UnitService:
    return UnitService(session=Connection())


UnitServiceDep = Annotated[UnitService, Depends(get_unit_service)]


@router.get("/units")
async def get_units(service: UnitServiceDep):
    return service.list_units()
