import json
from pathlib import Path
from typing import TypeVar, Generic, Type, Iterator, overload
from . import JsonData

T = TypeVar("T", bound=JsonData)

class JsonListData(Generic[T]):
    """No instantiate this class"""
    
    def __init__(self, items: list[T]):
        self._items: list[T] = items
    
    @classmethod
    def from_json(cls, model: Type[T], json: list[dict]) -> "JsonListData[T]":
        return cls([model.from_json(item) for item in json]) # type: ignore
    
    @classmethod
    def from_json_file(cls, model: Type[T], path: str|Path) -> "JsonListData[T]":
        
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
        
        JsonListData.save_items_in_file(path, self._items)

    
    def add_model(self, model: T) -> None:
        self._items.append(model)
    
    def remove_model(self, index: int) -> T:
        return self._items.pop(index)
    
    def __iter__(self) -> Iterator[T]:
        return iter(self._items)
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __contains__(self, item: T) -> bool:
        return item in self._items