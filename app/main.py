from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from .database.db import Base, engine, get_session
from app.database import models

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_db_and_tables():
    try:
        models.Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating the database tables {e}")
        raise

# Make sure DB is created before starting app
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting table creation..")
    create_db_and_tables()
    yield

logger.info("App started..")
app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"message": "FastAPI Test"}