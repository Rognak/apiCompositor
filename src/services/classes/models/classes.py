from extensions.database import Base
from sqlalchemy import Column, VARCHAR, SMALLINT, REAL, INT


class Classes(Base):
    __tablename__ = "Classes"

    cls = Column("class", VARCHAR(50), primary_key=True)
    type = Column(VARCHAR(2), nullable=False)
    country = Column(VARCHAR(20), nullable=False)
    num_guns = Column("numGuns", SMALLINT, nullable=True)
    bore = Column(REAL, nullable=True)
    displacement = Column(INT, nullable=True)
