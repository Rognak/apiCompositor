from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

USER = os.environ.get("POSTGRES_DB_USER", "outcomes")
PASSWORD = os.environ.get("POSTGRES_DB_PASSWORD", "outcomes123")
HOST = os.environ.get("POSTGRES_DB_HOST", "localhost")
DBNAME = os.environ.get("POSTGRES_DB_NAME", "outcomes")


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5433/{DBNAME}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
