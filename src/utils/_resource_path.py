import sys
from pathlib import Path

def resource_path(relative_path: str|Path) -> str:
    
    if hasattr(sys, "_MEIPASS"):
        return str(Path(sys._MEIPASS) / relative_path) #type: ignore

    return str(Path(relative_path))