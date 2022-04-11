from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from providers import ships_provider
from extensions.database import SessionLocal, engine
from extensions import database
from contracts.ships import Ships
from contracts.ships_filter import ShipsFilter


database.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/ships/", response_model=List[Ships])
def get_ships(filter: ShipsFilter, db: Session = Depends(get_db)):
    classes = ships_provider.get_ships(db, ships_filter=filter)
    return classes

