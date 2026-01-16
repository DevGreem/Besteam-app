from . import UserData, JsonListData

class AppData:
    
    
    def __init__(self) -> None:
        self.users: JsonListData[UserData] = JsonListData.from_json_file(UserData, 'users.json')
        