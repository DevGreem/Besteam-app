from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)
import logging
from . import GameList
from src import SteamClient

class OwnedGamePage(QWidget):
    
    def __init__(self, parent: QWidget | None = None, actual_game: int = -1) -> None:
        super().__init__(parent)
        
        self.actual_game = actual_game
    
    def load_game(self, game_id: int):
        client = SteamClient()
        
        app_details = client.apps.get_app_details(game_id)
        
        if not app_details:
            return
        
        self.actual_game = game_id