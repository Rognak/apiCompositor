from sqlalchemy.orm import Session
from contracts.ships_filter import ShipsFilter
from models import ships


def get_ships(db: Session, ships_filter: ShipsFilter = None):
    base_query = db.query(ships.Ships)

    if ships_filter is None:
        return base_query.all()

    if ships_filter.classes:
        base_query = base_query.filter(ships.Ships.cls.in_(ships_filter.classes))

    if ships_filter.names:
        base_query = base_query.filter(ships.Ships.name.in_(ships_filter.names))

    return base_query.all()



