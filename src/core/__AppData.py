from src import (
    UserData,
    JsonListData,
    AppConfig
)
from functools import lru_cache

class AppData:
    
    
    def __init__(self) -> None:
        self.app_config: AppConfig = AppConfig.from_json_file("src/data/app_config.json")
        self.users: JsonListData[UserData] = JsonListData.from_json_file(UserData, self.app_config.users_path)
    
    def save(self):
        self.app_config.save_in_file("src/data/app_config.json")
        self.users.save_in_file(self.app_config.users_path)
    
    @property
    def APP_NAME(self):
        return "Besteam"
    
    @property
    def APP_AUTHOR(self):
        return "DevGreem"
    

@lru_cache
def get_app_data() -> AppData:
    return AppData()