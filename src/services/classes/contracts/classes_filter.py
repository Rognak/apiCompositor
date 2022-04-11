from pydantic import BaseModel
from typing import List, Optional


class ClassesFilter(BaseModel):
    classes: Optional[List[str]] = None
    countries: Optional[List[str]] = None
    type: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "countries": ["USA"],
                "type": "bb",
            }
        }