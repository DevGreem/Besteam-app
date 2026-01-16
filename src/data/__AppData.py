from . import UserData

class AppData:
    
    users: list[UserData] = []
    
    def __init__(self) -> None:
        self.users = UserData.from_json("users.json") # type: ignore
