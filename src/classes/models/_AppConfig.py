from . import JsonData
from dataclasses import dataclass

@dataclass
class AppConfig(JsonData):
    
    users_path: str