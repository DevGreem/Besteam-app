from steam_web_api import Apps
from functools import lru_cache
from src.steam.models.games import GetAppDetails

class _Apps(Apps):
    
    @lru_cache
    def get_app_icon(self, appid: str, icon_hash: str) -> str:
        return f'https://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{icon_hash}.jpg'
    
    @lru_cache
    def get_app_details(self, app_id: int, country="US", filters: str | None = "basic") -> GetAppDetails: # type: ignore
        return GetAppDetails(super().get_app_details(app_id, country, filters))