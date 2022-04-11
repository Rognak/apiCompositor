from extensions.database import Base
from sqlalchemy import Column, VARCHAR, SMALLINT, REAL, INT


class Ships(Base):
    __tablename__ = "Ships"

    name = Column(VARCHAR(50), primary_key=True)
    cls = Column("class", VARCHAR(50), nullable=False)
    launched = Column(SMALLINT, nullable=True)
