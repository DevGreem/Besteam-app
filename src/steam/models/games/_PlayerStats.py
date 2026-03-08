from pydantic import BaseModel
from . import UserAchievement

class PlayerStats(BaseModel):
    steamID: str
    gameName: str
    achievements: list[UserAchievement]