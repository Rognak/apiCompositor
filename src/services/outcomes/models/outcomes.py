from extensions.database import Base
from sqlalchemy import Column, VARCHAR, SMALLINT, REAL, INT


class Outcomes(Base):
    __tablename__ = "Outcomes"

    ship = Column(VARCHAR(50), primary_key=True)
    battle = Column(VARCHAR(20), primary_key=True)
    result = Column(VARCHAR(10), nullable=False)
