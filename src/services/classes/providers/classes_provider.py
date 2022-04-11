from sqlalchemy.orm import Session
from contracts.classes_filter import ClassesFilter
from models import classes


def get_classes(db: Session, classes_filter: ClassesFilter = None):
    base_query = db.query(classes.Classes)

    if classes_filter is None:
        return base_query.all()

    if classes_filter.classes:
        base_query = base_query.filter(classes.Classes.cls.in_(classes_filter.classes))

    if classes_filter.countries:
        base_query = base_query.filter(classes.Classes.country.in_(classes_filter.countries))

    if classes_filter.type:
        base_query = base_query.filter(classes_filter.type == classes_filter.type)

    return base_query.all()



