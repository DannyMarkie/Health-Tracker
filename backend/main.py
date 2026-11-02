# from database import get_database_connection
from api.v1 import ingredients, units
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping/")
async def get_ping():
    return "pong"

app.include_router(ingredients.router, prefix="/api/v1")
app.include_router(units.router, prefix="/api/v1")