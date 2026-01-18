from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Literal

class EnvVars(BaseSettings):
    '''
    Class for manage Environment Variables
    '''
    
    def __init__(self):
        super().__init__(_case_sensitive=False, _env_file=".env")
        
    steam_api_key: str
    env: Literal["testing", "builded"]
    
    @property
    def api_key(self) -> str:
        
        return self.steam_api_key
    
    def is_testing(self) -> bool:
        return self.env == "testing"
    
@lru_cache
def get_env_vars() -> EnvVars:
    return EnvVars() # type: ignore
