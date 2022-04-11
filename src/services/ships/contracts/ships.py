from pydantic import BaseModel


class Ships(BaseModel):
    name: str
    cls: str
    launched: int

    class Config:
        orm_mode = True
