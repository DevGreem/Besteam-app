from pydantic import BaseModel
from typing import Optional

class Player(BaseModel):
    steamid: str
    communityvisibilitystate: int
    profilestate: int
    personaname: str
    profileurl: str
    avatar: str
    avatarmedium: str
    avatarfull: str
    avatarhash: str
    lastlogoff: int
    personastate: int
    primaryclanid: str
    timecreated: int
    personastateflags: int
    loccountrycode: Optional[str] = None