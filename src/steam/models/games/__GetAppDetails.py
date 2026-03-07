from pydantic import BaseModel


class Requirements(BaseModel):
    minimum: str
    recommended: str


class Data(BaseModel):
    type: str
    name: str
    steam_appid: int
    required_age: int
    is_free: bool
    controller_support: str
    dlc: list[int]
    detailed_description: str
    about_the_game: str
    short_description: str
    supported_languages: str
    header_image: str
    capsule_image: str
    capsule_imagev5: str
    website: str
    pc_requirements: Requirements
    mac_requirements: Requirements
    linux_requirements: Requirements


class AppDetail(BaseModel):
    success: bool
    data: Data

class GetAppDetails(dict[str, AppDetail]): ...