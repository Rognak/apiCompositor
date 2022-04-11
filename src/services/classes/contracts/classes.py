from pydantic import BaseModel


class Classes(BaseModel):
    cls: str
    type: str
    country: str
    num_guns: int
    bore: float
    displacement: int

    class Config:
        orm_mode = True