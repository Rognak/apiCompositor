from pydantic import BaseModel
from typing import List, Optional


class BattlesFilter(BaseModel):
    names: Optional[List[str]] = None

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "countries": ["USA"],
    #             "type": "bb",
    #         }
    #     }