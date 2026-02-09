from steam_web_api import Client
from . import _Users, _Apps
from src import AppData

class SteamClient:
    
    """Steam API client"""
    #TODO: https://store.steampowered.com/api/appdetails?appids=570
    def __init__(self, headers: dict = {}):
        """Constructor for Steam API client"""
        
        KEY = AppData.app_config.steam_api_key
    
        if not KEY:
            return
        
        self.__client = Client(KEY, headers=headers)
        self.__users = _Users(self.__client)
        self.__apps = _Apps(self.__client)

    @property
    def users(self) -> _Users:
        return self.__users

    @property
    def apps(self) -> _Apps:
        return self.__apps