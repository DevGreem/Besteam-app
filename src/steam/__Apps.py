from steam_web_api import Apps
import requests

class _Apps(Apps):
    
    def get_app_icon(self, appid: str, icon_hash: str) -> str:
        return f'https://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{icon_hash}.jpg'