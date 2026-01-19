from PyQt6.QtWidgets import QMenu

class SteamMenu(QMenu):
    
    def __init__(self, parent=None):
        super().__init__("Besteam", parent)
        self.setEnabled(False)