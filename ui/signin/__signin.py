from PyQt6.QtWidgets import * # type: ignore
from src import SteamClient, AppData

class SignInContainer(QWidget):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        self.users_container = QWidget()
        
        self.users_layout = QGridLayout(self.users_container)

        steam: SteamClient = SteamClient()
        
        self.users_details = steam.users.get_user_details(
            ",".join(
                [
                    str(item["id"])
                    for item in 
                    AppData.users.models_dump()
                ]
            ),
            single=False
        )
        
        print(self.users_details)
