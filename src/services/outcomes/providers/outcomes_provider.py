from sqlalchemy.orm import Session
from contracts.outcomes_filter import OutcomesFilter
from models import outcomes


def get_outcomes(db: Session, outcomes_filter: OutcomesFilter = None):
    base_query = db.query(outcomes.Outcomes)

    if outcomes_filter is None:
        return base_query.all()

    if outcomes_filter.ships:
        base_query = base_query.filter(outcomes.Outcomes.ship.in_(outcomes_filter.ships))

    if outcomes_filter.battles:
        base_query = base_query.filter(outcomes.Outcomes.battle.in_(outcomes_filter.battles))

    if outcomes_filter.results:
        base_query = base_query.filter(outcomes.Outcomes.result.in_(outcomes_filter.results))

    return base_query.all()



