import json
from pathlib import Path
from abc import ABC
from typing import Self
from pydantic import BaseModel

class JsonData(ABC, BaseModel):

    @classmethod
    def from_json_file(cls, path: str|Path) -> Self:
        
        with open(path, "r") as file:
            data = json.load(file)
        
        return cls.model_validate(data)
    
    def save_in_file(self, path: str | Path) -> None:
        
        with open(path, "w") as file:
            json.dump(self.model_dump_json(), file, indent=4)
