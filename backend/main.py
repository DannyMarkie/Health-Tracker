from api.v1 import ingredients, units
from database import SessionDep
from fastapi import FastAPI
from sqlalchemy import text

app = FastAPI()


@app.get("/")
def health(session: SessionDep):
    session.execute(text("SELECT 1"))
    return "Operational"


app.include_router(ingredients.router, prefix="/api/v1")
app.include_router(units.router, prefix="/api/v1")
