from pydantic import BaseModel
from typing import List, Optional


class OutcomesFilter(BaseModel):
    ships: Optional[List[str]] = None
    battles: Optional[List[str]] = None
    results: Optional[List[str]] = None

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "countries": ["USA"],
    #             "type": "bb",
    #         }
    #     }