from . import JsonData
from dataclasses import dataclass

class AppConfig(JsonData):
    
    users_path: str