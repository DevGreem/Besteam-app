import os
from steam_web_api import Steam

class SteamClient(Steam):
    
    def __init__(self):
        
        KEY = os.environ.get('STEAM_API_KEY')
    
        if not KEY:
            return
        
        super().__init__(KEY)
