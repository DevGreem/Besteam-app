from pydantic import BaseModel
from . import PlayerStats

class GetUserStats(BaseModel):
    playerstats: PlayerStats