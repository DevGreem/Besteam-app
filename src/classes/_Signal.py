from typing import TypeVarTuple, Protocol, Callable, Optional

Ts = TypeVarTuple("Ts")

class Signal(Protocol[*Ts]):
    """Class for variable typing

    Args:
        Protocol (_type_): _description_
    """
    
    def emit(self, *args: *Ts): ...
    
    def connect(self, slot: Callable) -> tuple[*Ts]: ...
    
    def disconnect(self, handler: Optional[Callable]): ...