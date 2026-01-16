from . import JsonData
from dataclasses import dataclass

class UserData(JsonData):
    id: int
    default_login: bool
    