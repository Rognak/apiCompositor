from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from providers import classes_provider
from extensions.database import SessionLocal, engine
from extensions import database
from contracts.classes import Classes
from contracts.classes_filter import ClassesFilter


database.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/classes/", response_model=List[Classes])
def get_classes(filter: ClassesFilter, db: Session = Depends(get_db)):
    classes = classes_provider.get_classes(db, classes_filter=filter)
    return classes

