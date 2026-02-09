from src import (
    UserData,
    JsonListData,
    AppConfig
)
from functools import lru_cache
from pathlib import Path
import platformdirs
import os
import json

class AppData:
    
    
    def __init__(self) -> None:
        self.app_config: AppConfig = AppConfig.from_json_file(self.get_app_config_path())
        self.users: JsonListData[UserData] = JsonListData.from_json_file(UserData, self.get_users_path())
    
    def save(self):
        self.app_config.save_in_file("src/data/app_config.json")
        self.users.save_in_file(self.get_users_path())
    
    @property
    def APP_NAME(self):
        return "Besteam"
    
    @property
    def APP_AUTHOR(self):
        return "DevGreem"

    def get_config_dir(self) -> Path:
        
        path = Path(platformdirs.user_config_dir(self.APP_NAME, self.APP_AUTHOR))
        
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        
        return path

    def get_data_dir(self) -> Path:
        
        path = Path(platformdirs.user_data_dir(self.APP_NAME, self.APP_AUTHOR))
        
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        
        return path

    def get_app_config_path(self) -> Path:
        path = self.get_config_dir() / "app_config.json"
        
        if not path.exists():
            path.write_text(json.dumps({
                "environment": "builded",
                "steam_api_key": "",
                
            }, indent=4))
        
        return path

    def get_users_path(self) -> Path:
        
        path = self.get_data_dir() / "users.json"
        
        if not path.exists():
            path.write_text("[]")
        
        return path
    

@lru_cache
def get_app_data() -> AppData:
    return AppData()