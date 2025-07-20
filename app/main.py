from fastapi import FastAPI
from app.routers import haunted_locations
from app.db_models.database import create_db_and_tables
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(haunted_locations.router)


@app.get("/")
def root():
    return {"message": "Hello world!"}
