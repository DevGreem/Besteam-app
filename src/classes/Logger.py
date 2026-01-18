from src import EnvVars
from typing import Any

def log(text: Any):
        
    if EnvVars.is_testing():
        print(text)