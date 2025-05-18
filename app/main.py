from fastapi import FastAPI
from app.db.database import database
from app.api.routes import router
from app.db.models import metadata
from sqlalchemy import create_engine
from app.config import settings

app = FastAPI()
app.include_router(router)

engine = create_engine(settings.DATABASE_URL.replace("+asyncpg", ""))

@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()