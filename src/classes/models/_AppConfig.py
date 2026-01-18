from . import JsonData
from dataclasses import dataclass
from typing import Literal

class AppConfig(JsonData):
    
    environment: Literal["testing", "builded"]
    steam_api_key: str
    users_path: str