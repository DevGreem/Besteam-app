import json
from pathlib import Path
from typing import TypeVar, Generic, Type
from . import JsonData

T = TypeVar("T", bound=JsonData)

class JsonListData(Generic[T]):
    """No instantiate this class"""
    
    def __init__(self, items: list[T]):
        self.items = items
    
    @classmethod
    def from_json(cls, model: Type[T], path: str|Path) -> "JsonListData[T]":
        
        with open(path, "r") as file:
            data = json.load(file)
        
        if not isinstance(data, list):
            raise TypeError("I await an JSON array!")
        
        items: list[T] = [model.from_json(item) for item in data] # type: ignore
        
        return cls(items)
    
    @classmethod
    def save_items_in_file(cls, path: str | Path, items: list[T]) -> None:
        
        with open(path, "w") as file:
            json.dump([item.to_json() for item in items], file, indent=4)

    def save_in_file(self, path: str | Path):
        
        JsonListData.save_items_in_file(path, self.items)