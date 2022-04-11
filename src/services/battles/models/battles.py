from extensions.database import Base
from sqlalchemy import Column, VARCHAR, DateTime


class Battles(Base):
    __tablename__ = "Battles"

    name = Column(VARCHAR(50), primary_key=True)
    date = Column(DateTime, nullable=False)
