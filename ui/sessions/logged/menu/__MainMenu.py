from PyQt6.QtWidgets import (
    QMenuBar,
    QWidget,
    QSizePolicy,
    QWidgetAction
)
from PyQt6.QtCore import Qt
from . import *

class MainMenu(QMenuBar):
    
    def __init__(self, native: bool = True, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setNativeMenuBar(native)
        self.__build_actions()
    
    def __build_actions(self):
        self.besteam_menu_icon = SteamMenuIcon(self)
        self.addMenu(self.besteam_menu_icon)
        
        self.besteam_menu = SteamMenu(self)
        self.addMenu(self.besteam_menu)
        
        self.spacer = QWidget()
        self.spacer.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Expanding
        )
        self.spacer.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        
        self.spacer_action = QWidgetAction(self)
        self.spacer_action.setDefaultWidget(self.spacer)
        
        self.addAction(self.spacer_action)
        
        self.test_menu = SteamMenu(self)
        self.addMenu(self.test_menu)
        
        self.setCornerWidget(self.test_menu, Qt.Corner.TopRightCorner)