import json
from pathlib import Path
from abc import ABC

class JsonData(ABC):
    
    @classmethod
    def from_json(cls, json: dict) -> "JsonData":
        return cls(**json)

    @classmethod
    def from_json_file(cls, path: str|Path) -> "JsonData":
        
        with open(path, "r") as file:
            data = json.load(file)
        
        return cls(**data)
    
    def to_json(self) -> dict:
        return self.__dict__
    
    def save_in_file(self, path: str | Path) -> None:
        
        with open(path, "w") as file:
            json.dump(self.to_json(), file, indent=4)
