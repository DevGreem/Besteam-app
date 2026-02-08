from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSignal

from src import AccountManager, Signal
from src.steam import Player
import logging

from .components import UsersGrid

class SignInContainer(QWidget):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        self.users_container = QWidget(self)
        self.users_container.resize(500, 500)
        
        self.users_grid = UsersGrid(3, 3, self.users_container)
        
        self.users_grid.clicked_user.connect(self._on_press_user)
        
        self.users_container.setLayout(self.users_grid)
        
    def _on_press_user(self, user: Player):
        logging.log(0, f'Logged with {user.steamid}')
        AccountManager.login_user(user.steamid)