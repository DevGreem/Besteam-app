from steam_web_api import Users
from .models import GetUserDetailsData
import logging
from functools import lru_cache
from typing import overload, Literal

class _Users(Users):
    
    @overload
    def get_user_details(self, steam_id: str, single: Literal[True]) -> GetUserDetailsData: ...
    
    @overload
    def get_user_details(self, steam_ids: list[str], single: Literal[False]) -> GetUserDetailsData: ...
    
    
    def get_user_details(self, steam_id: str, single=True) -> GetUserDetailsData: # type: ignore
        
        users = steam_id if single else ",".join(steam_id)
        
        logging.log(0, users)
        
        data = super().get_user_details(users, single)
        
        logging.log(0, data)
        
        return GetUserDetailsData(**data)