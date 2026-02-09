from PyQt6.QtGui import (
    QResizeEvent,
    QShowEvent
)
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout
)
from PyQt6.QtWidgets import * # type: ignore
from src import AppData
from . import (
    WindowWrapper
)
from ui.components.menu import TwoSideMenu
import logging

class LoggedMainWindow(WindowWrapper):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        self.right_layout = QVBoxLayout(self)
        self.divided_layout = QHBoxLayout(self)
        self.__load_sections()
        self.showMaximized()
        self.setLayout(self.right_layout)
        
        
    
    def __load_sections(self):
                
        self.menu = TwoSideMenu(self)
        self.menu.show()
        
        self.content = QWidget(self)
        self.content.setLayout(self.divided_layout)
        self.content.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum
        )
        
        self.right_layout.addWidget(self.menu)
        self.right_layout.addWidget(self.content)
        
        self.__load_content()
    
    def __load_content(self):
        
        self.games = QWidget(self.content)
        self.game_info = QWidget(self.content)
        
        self.divided_layout.addWidget(self.games)
        self.divided_layout.addWidget(self.game_info)
    
    def resizeEvent(self, a0: QResizeEvent | None) -> None:
        super().resizeEvent(a0)
        
        self.menu.setFixedWidth(self.width())
        logging.debug(a0.size()) # type: ignore