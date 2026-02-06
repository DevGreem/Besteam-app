from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QIcon

class SteamMenuIcon(QMenu):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setEnabled(False)
        self.setIcon(QIcon("assets/menu/icon.png"))