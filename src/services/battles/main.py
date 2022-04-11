from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from providers import battles_provider
from extensions.database import SessionLocal, engine
from extensions import database
from contracts.battles import Battles
from contracts.battles_filter import BattlesFilter
from compositors.battle_history_compositor import BattleHistoryCompositor


from clients.classes_api_client.client import Client as ClassesClient
from clients.ships_api_client.client import Client as ShipsClient
from clients.outcomes_api_client.client import Client as OutcomesClient


database.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def cls_client():
    client = ClassesClient()
    return client

def ship_client():
    client = ShipsClient()
    return client

def outcome_client():
    client = OutcomesClient()
    return client


@app.post("/battles/", response_model=List[Battles])
def get_ships(filter: BattlesFilter, db: Session = Depends(get_db)):
    classes = battles_provider.get_battles(db, battles_filter=filter)
    return classes


@app.get("/battles-history/")
async def get_history(db: Session = Depends(get_db),
                classes_client: ClassesClient = Depends(cls_client),
                ships_client: ShipsClient = Depends(ship_client),
                outcomes_client: OutcomesClient = Depends(outcome_client)
                ):

    compositor = BattleHistoryCompositor(classes_client=classes_client,
                                         ships_client=ships_client,
                                         outcomes_client=outcomes_client)

    result = await compositor.composite(db)

    return result



