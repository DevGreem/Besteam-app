from steam_web_api import Users
from .models import GetUserDetailsData
from src import Logger

class _Users(Users):
    
    def get_user_details(self, steam_id: str, single=True) -> GetUserDetailsData: # type: ignore
        
        data = super().get_user_details(steam_id, single)
        
        Logger.log(data)
        
        return GetUserDetailsData(**data)