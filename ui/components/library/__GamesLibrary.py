from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout
)
import logging

class GamesLibrary(QWidget):
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.divided_layout = QHBoxLayout(self)
        
        self.__load_sections()
        
        self.setLayout(self.divided_layout)
        
        logging.debug("Loaded library")
    
    def __load_sections(self):
        
        self.games = QWidget(self)
        self.games.setMaximumWidth(400)
        
        _ = self.__load_games()
        
        self.game_info = QWidget(self)
        
        self.divided_layout.addWidget(self.games)
    
    async def __load_games(self):
        pass
    
    def show_game_info(self, game_id: int):
        pass