from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import * # type: ignore
from src import AppData
from . import (
    WindowWrapper
)
from . import MainMenu

class LoggedMainWindow(WindowWrapper):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)

        self.menu = MainMenu(parent=self)
        self.setMenuBar(self.menu)