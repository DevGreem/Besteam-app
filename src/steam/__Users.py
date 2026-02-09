from steam_web_api import Users
from .models.users import GetUserDetailsData
import logging
from typing import overload, Literal
from src.steam.models.games import SimpleGamesOwnedList, GamesOwnedList

class _Users(Users):
    
    @overload
    def get_user_details(self, steam_id: str, single: Literal[True]) -> GetUserDetailsData: ...
    
    @overload
    def get_user_details(self, steam_ids: list[str], single: Literal[False]) -> GetUserDetailsData: ...
    
    
    def get_user_details(self, steam_id: str, single=True) -> GetUserDetailsData: # type: ignore
        
        users = steam_id if single else ",".join(steam_id)
        
        logging.debug(f"Raw Users: {users}")
        
        data = super().get_user_details(users, single)
        
        logging.debug(f"Loaded Users: {data}")
        
        return GetUserDetailsData(**data)
    
    @overload
    def get_owned_games(self, steam_id: str, include_appinfo: Literal[True], include_free_games: bool = True) -> GamesOwnedList: ...
    
    @overload
    def get_owned_games(self, steam_id: str, include_appinfo: Literal[False], include_free_games: bool = True) -> SimpleGamesOwnedList: ...
    
    def get_owned_games(self, steam_id: str, include_appinfo: bool = True, includ_free_games: bool = True) -> GamesOwnedList|SimpleGamesOwnedList: # type: ignore        
        
        data = super().get_owned_games(steam_id, include_appinfo, includ_free_games)
        
        logging.debug("Games data:", data)
        
        if include_appinfo:
            return GamesOwnedList(**data)
        
        return SimpleGamesOwnedList(**data)