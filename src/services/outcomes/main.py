from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from providers import outcomes_provider
from extensions.database import SessionLocal, engine
from extensions import database
from contracts.outcomes import Outcomes
from contracts.outcomes_filter import OutcomesFilter


database.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/outcomes/", response_model=List[Outcomes])
def get_outcomes(filter: OutcomesFilter, db: Session = Depends(get_db)):
    classes = outcomes_provider.get_outcomes(db, outcomes_filter=filter)
    return classes

