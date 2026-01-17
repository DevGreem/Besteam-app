from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import * # type: ignore
from src import AppData
from . import WindowWrapper, LoginWindow

class MainWindow(WindowWrapper):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        data: AppData = AppData()
        
        self.login_window = LoginWindow(self)
        
        if len(data.users) > 0:
            return
    
    def resizeEvent(self, a0: QResizeEvent | None) -> None:
        
        if not a0:
            return
        
        self.login_window.resize(a0.size())
        return super().resizeEvent(a0)
        