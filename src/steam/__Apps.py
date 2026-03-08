from steam_web_api import Apps
from src.steam.models.games import (
    GetAppDetails,
    GetUserStats,
    PlayerStats,
    GameData
)
from typing import Any
import logging
import json

class _Apps(Apps):
    
    def get_app_icon(self, appid: str, icon_hash: str) -> str:
        return f'https://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{icon_hash}.jpg'
    
    def get_app_details(self, app_id: int, country="US", filters: str | None = "basic") -> GameData: # type: ignore
        app_details: GetAppDetails = super().get_app_details(app_id, country, filters)
        logging.debug(f"Requested game: {app_id}\nLoaded info: {json.dumps(app_details)}")
        
        return GameData(**app_details.get(str(app_id)).get('data')) # type: ignore
    
    def get_user_stats(self, steam_id: str, app_id: int) -> PlayerStats: # type: ignore
        return PlayerStats(**super().get_user_stats(steam_id, app_id)['playerstats']) # type: ignore

    def get_global_achievement_percentages_for_app(self, game_id: int):
        
        response = self.__client.request(
            'get',
            'ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2',
            params={'gameid': game_id}
        )
        
        return response