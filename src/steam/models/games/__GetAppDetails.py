from pydantic import BaseModel
from typing import Optional

class Requirements(BaseModel):
    minimum: str
    recommended: Optional[str] = None


class GameData(BaseModel):
    type: str
    name: str
    steam_appid: int
    required_age: int
    is_free: bool
    controller_support: Optional[str] = None
    dlc: Optional[list[int]] = None
    detailed_description: str
    about_the_game: str
    short_description: str
    supported_languages: Optional[str] = None
    header_image: str
    capsule_image: str
    capsule_imagev5: str
    website: Optional[str] = None
    pc_requirements: Requirements|list = []
    mac_requirements: Requirements|list = []
    linux_requirements: Requirements|list = []


class AppDetail(BaseModel):
    success: bool
    data: GameData

GetAppDetails = dict[str, AppDetail]