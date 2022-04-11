from pydantic import BaseModel


class Outcomes(BaseModel):
    ship: str
    battle: str
    result: str

    class Config:
        orm_mode = True
