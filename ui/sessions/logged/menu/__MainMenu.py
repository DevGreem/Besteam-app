from PyQt6.QtWidgets import (
    QMenuBar,
    QWidget,
    QMenu,
    QHBoxLayout,
    QLabel,
    QWidgetAction
)
from ui.components import ImageLabel
from . import *

class MainMenu(QMenuBar):
    
    def __init__(self, native: bool = True, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setNativeMenuBar(native)
        self.__build_actions()
    
    def __build_actions(self):
        self.steam_menu = SteamMenu(self)
        self.addMenu(self.steam_menu)