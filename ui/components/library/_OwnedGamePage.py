from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QSizePolicy
)
import logging
from src import SteamClient, AccountManager
from src.steam.models.games import (
    GetUserStats,
    GameData
)
from ui.components import QUrlImage, UrlImageLabel

class OwnedGamePage(QWidget):
    
    _actual_game: int = -1
    """Actual game **ID**:
    
    if **ID** = -1: None game selected
    
    if **ID** = -2: Error on loading game or this game doesn't exists
    """
    
    _game_details: GameData
    _user_stats: GetUserStats
    
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.widget_layout = QVBoxLayout()
        
        self.setLayout(self.widget_layout)
        self.__portrait: UrlImageLabel = UrlImageLabel(self)
    
    @property
    def actual_game(self):
        return self._actual_game
    
    def set_game(self, game_id: int):
        self._actual_game = game_id
        self.__load_game()
    
    def __load_game(self):
        client = SteamClient()
        
        app_details: GameData = client.apps.get_app_details(self._actual_game)
                
        if not app_details:
            self._actual_game = -2
            return
        
        self._game_details = app_details
        self.__load_portrait()
    
    def __load_achievements(self):
        pass
    
    def __load_user_stats(self):
        client = SteamClient()
        
        user_stats = client.apps.get_user_stats(AccountManager.actual_user_id, self._actual_game)
    
    def __load_portrait(self):
        self.__portrait.setPixmapUrl(self._game_details.header_image)
        self.__portrait.setMaximumHeight(500)
        self.__portrait.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )
        
        self.widget_layout.addWidget(self.__portrait)
    
    def __load_content(self):
        pass