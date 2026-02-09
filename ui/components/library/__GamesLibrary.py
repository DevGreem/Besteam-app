from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout
)
import logging
from . import GameList

class GamesLibrary(QWidget):
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.divided_layout = QHBoxLayout()
        
        self.__load_sections()
        
        self.setLayout(self.divided_layout)
        
        logging.debug("Loaded library")
    
    def __load_sections(self):
        
        self.games = GameList(self)
        
        self.game_info = QWidget(self)
        
        self.divided_layout.addWidget(self.games)
        self.divided_layout.addWidget(self.game_info)