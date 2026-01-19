from PyQt6.QtCore import QObject
from . import UnloggedMainWindow, LoggedMainWindow
from src import AccountManager

class AppController(QObject):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.unlogged = UnloggedMainWindow()
        self.unlogged.show()
        
        AccountManager.on_user_logged.connect(self._on_user_logged)
        AccountManager.on_user_logout.connect(self._on_user_logout)
    
    def _on_user_logged(self, user: str):
        self.logged = LoggedMainWindow()
        self.logged.showMaximized()
        self.unlogged.close()
    
    def _on_user_logout(self, user: str):
        self.logged.close()
        self.unlogged.show()
        self.logged.deleteLater()