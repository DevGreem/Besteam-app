from PyQt6.QtGui import QResizeEvent, QShowEvent
from PyQt6.QtWidgets import * # type: ignore
from src import AppData
from . import (
    WindowWrapper
)
from . import MainMenu, TwoSideMenu
import logging

class LoggedMainWindow(WindowWrapper):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        self.menu = MainMenu(False, parent=self)
        self.setMenuBar(self.menu)
        
        self.other_menu = TwoSideMenu(self)
        
        self.showMaximized()
        self.other_menu.show()
        
    
    def resizeEvent(self, a0: QResizeEvent | None) -> None:
        super().resizeEvent(a0)
        
        self.other_menu.setFixedWidth(self.width())
        logging.log(0, a0.size()) # type: ignore