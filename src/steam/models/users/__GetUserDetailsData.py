from pydantic import BaseModel
from . import Player

class GetUserDetailsData(BaseModel):
    players: list[Player]