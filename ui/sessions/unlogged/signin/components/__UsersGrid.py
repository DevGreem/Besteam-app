from PyQt6.QtWidgets import QGridLayout, QWidget
from PyQt6.QtCore import pyqtSignal
from src import SteamClient, AppData, Signal
from src.steam import GetUserDetailsData, Player
from . import UserBigCard
from typing import cast

class UsersGrid(QGridLayout):
    
    clicked_user: Signal[Player] = cast(Signal[Player], pyqtSignal(Player))
    
    def __init__(self, columns: int, rows: int, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.columns = columns
        self.rows = rows
        
        steam: SteamClient = SteamClient()
        
        self.users_details: GetUserDetailsData = steam.users.get_user_details(
            [str(item['id']) for item in AppData.users.models_dump()],
            single=False
        )
        
        self.load_users()
        
    def load_users(self):
        
        for index, user in enumerate(self.users_details.players):
            row = index // self.rows
            column = index % self.columns
            
            user_container = UserBigCard(user, self.parentWidget())
            user_container.clicked.connect(self._on_click_user)
            
            self.addWidget(user_container, row, column)
    
    def _on_click_user(self, user: Player):
        self.clicked_user.emit(user)