from sqlalchemy.orm import Session
from contracts.battles_filter import BattlesFilter
from models import battles


def get_battles(db: Session, battles_filter: BattlesFilter = None):
    base_query = db.query(battles.Battles)

    if battles_filter is None:
        return base_query.all()

    if battles_filter.names:
        base_query = base_query.filter(battles.Battles.name.in_(battles_filter.names))

    return base_query.all()



