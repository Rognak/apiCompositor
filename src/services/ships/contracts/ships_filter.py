from pydantic import BaseModel
from typing import List, Optional


class ShipsFilter(BaseModel):
    classes: Optional[List[str]] = None
    names: Optional[List[str]] = None

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "countries": ["USA"],
    #             "type": "bb",
    #         }
    #     }