from PyQt6.QtGui import QResizeEvent, QShowEvent
from PyQt6.QtWidgets import * # type: ignore
from src import AppData, Logger
from . import (
    WindowWrapper
)
from . import MainMenu, TwoSideMenu

class LoggedMainWindow(WindowWrapper):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        self.menu = MainMenu(False, parent=self)
        self.setMenuBar(self.menu)
        
        self.other_menu = TwoSideMenu(self)
        self.other_menu.show()
        
        self.showMaximized()
        
    
    def resizeEvent(self, a0: QResizeEvent | None) -> None:
        super().resizeEvent(a0)
        
        self.other_menu.resize(self.width(), self.other_menu.height())
        Logger.log(a0.size()) # type: ignore