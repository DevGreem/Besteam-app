from pydantic import BaseModel
from typing import Literal

class UserAchievement(BaseModel):
    name: str
    achieved: Literal[0, 1]