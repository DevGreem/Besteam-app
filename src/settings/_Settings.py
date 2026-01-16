from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    '''
    Class for manage Environment Variables
    '''
    
    def __init__(self):
        super().__init__(_case_sensitive=False, _env_file=".env")
        
    steam_api_key: str
    
    @property
    def api_key(self) -> str:
        
        return self.steam_api_key
    
@lru_cache
def get_settings() -> Settings:
    return Settings() # type: ignore
