import os
from steam_web_api import Client, Apps
from . import _Users

class SteamClient:
    
    """Steam API client"""

    def __init__(self, headers: dict = {}):
        """Constructor for Steam API client"""
        
        KEY = os.environ.get('STEAM_API_KEY')
    
        if not KEY:
            return
        
        client = Client(KEY, headers=headers)
        self.__users = _Users(client)
        self.__apps = Apps(client)

    @property
    def users(self) -> _Users:
        return self.__users

    @property
    def apps(self) -> Apps:
        return self.__apps