from typing import (
    TypeVarTuple,
    Protocol,
    Callable,
    Optional,
    Any
)
from PyQt6.QtCore import pyqtSignal

Ts = TypeVarTuple("Ts")

#* Old code
# @runtime_checkable
# class Signal(Protocol[*Ts]):
#     """Class for variable typing

#     Args:
#         Protocol (_type_): _description_
#     """
    
#     def emit(self, *args: *Ts): ...
    
#     def connect(self, slot: Callable[[*Ts], Any]): ...
    
#     def disconnect(self, handler: Optional[Callable[[*Ts], Any]]): ...


class Signal(Protocol[*Ts]):
    
    def emit(self, *args: *Ts): ...
    
    def connect(self, slot: Callable[[*Ts], Any]): ... # type: ignore
    
    def disconnect(self, handler: Optional[Callable[[*Ts], Any]]): ... # type: ignore
    
    @classmethod
    def create(cls, *types: Any, name: str = "") -> "Signal":
        """DO NOT USE IF YOU ALREADY INITIALIZE THE VARIABLE WITH SIGNAL CLASS

        Args:
            name (str, optional): _description_. Defaults to "".

        Returns:
            Signal: _description_
        """
        
        if not name:
            import uuid
            name = uuid.uuid4().hex
        
        return pyqtSignal(*types, name=name) #type: ignore

#* Helper
# def signal[*Ts](*types: type, name: str = "") -> Signal[*Ts]: # type: ignore
#     return pyqtSignal(*types, name=name) # type: ignore

ola = pyqtSignal(int)
