from typing import (
    TypeVarTuple,
    Protocol,
    Callable,
    Optional,
    Any
)

Ts = TypeVarTuple("Ts")

class Signal(Protocol[*Ts]):
    """Class for variable typing

    Args:
        Protocol (_type_): _description_
    """
    
    def emit(self, *args: *Ts): ...
    
    def connect(self, slot: Callable[[*Ts], Any]): ...
    
    def disconnect(self, handler: Optional[Callable[[*Ts], Any]]): ...