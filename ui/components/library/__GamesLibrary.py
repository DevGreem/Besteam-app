from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout
)
import logging
from . import OwnedGamePage, GameList

class GamesLibrary(QWidget):
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.divided_layout = QHBoxLayout()
        
        self.__load_sections()
        
        self.setLayout(self.divided_layout)
        
        logging.debug("Loaded library")
    
    def __load_sections(self):
        
        self.games = GameList(self)
        self.games.on_press_game.connect(self._on_press_game)
        
        self.game_info = OwnedGamePage(self)
        
        self.divided_layout.addWidget(self.games)
        self.divided_layout.addWidget(self.game_info)
    
    def _on_press_game(self, id: int):
        logging.debug(f"Pressed game: {id}")
        self.game_info.set_game(id)