from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from .database.db import Base, engine
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

# Create DB and tables on startup
def startup_event():
    logger.info("Starting up...")
    create_db_and_tables()
    
app = FastAPI(on_startup=[startup_event])

@app.get("/")
def home():
    return {"message": "FastAPI Test"}