from PyQt5.QtWidgets import * # type: ignore
from src import AppData
from . import WindowWrapper, LoginWindow

class MainWindow(WindowWrapper):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        data: AppData = AppData()
        
        self.login_window = LoginWindow(self)
        
        if len(data.users) > 0:
            return
        