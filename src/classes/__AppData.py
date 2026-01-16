from . import (
    UserData,
    JsonListData,
    AppConfig
)

class AppData:
    
    def __init__(self) -> None:
        self.app_config: AppConfig = AppConfig.from_json_file("src/data/app_config.json")
        self.users: JsonListData[UserData] = JsonListData.from_json_file(UserData, self.app_config.users_path)
    
    def save(self):
        
        self.users.save_in_file(self.app_config.users_path)