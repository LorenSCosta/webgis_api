import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

APP_PROFILE = os.getenv("APP_PROFILE", "DEV")
DATABASE_URL_ENV = os.getenv("DATABASE_URL")

if APP_PROFILE == "DEV":
    SQLALCHEMY_DATABASE_URL = DATABASE_URL_ENV or "postgresql://postgres:bdtads2025@localhost/webgis"
else:
    SQLALCHEMY_DATABASE_URL = DATABASE_URL_ENV or "postgresql://localhost/webgis"

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
