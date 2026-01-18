from . import AppData
from typing import Any

def log(text: Any):
        
    if AppData.app_config.environment == "testing":
        print(text)