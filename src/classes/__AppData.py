from . import (
    UserData,
    JsonListData,
    AppConfig
)
from functools import lru_cache

class AppData:
    
    def __init__(self) -> None:
        self.app_config: AppConfig = AppConfig.from_json_file("src/data/app_config.json")
        self.users: JsonListData[UserData] = JsonListData.from_json_file(UserData, self.app_config.users_path)
        self.__actual_user: int = -1
    
    def save(self):
        
        self.users.save_in_file(self.app_config.users_path)
    
    @property
    def actual_user(self) -> int:
        return self.__actual_user
    
    def login_user(self, new_user_id: int):
        
        if new_user_id <= 0:
            raise Exception("You cannot introduce a user with id 0 or less!")
        
        self.__actual_user = new_user_id
    
    def logout_user(self):
        self.__actual_user = -1

@lru_cache
def get_app_data() -> AppData:
    return AppData()