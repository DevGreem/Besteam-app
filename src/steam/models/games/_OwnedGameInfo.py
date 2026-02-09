from pydantic import BaseModel
from typing import Optional

class SimpleOwnedGameInfo(BaseModel):
    appid: int
    playtime_forever: int

class OwnedGameInfo(SimpleOwnedGameInfo):
    name: str
    img_icon_url: str
    content_descriptorids: Optional[list[int]] = None