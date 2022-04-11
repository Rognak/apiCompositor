import datetime

from pydantic import BaseModel


class Battles(BaseModel):
    name: str
    date: datetime.date

    class Config:
        orm_mode = True
