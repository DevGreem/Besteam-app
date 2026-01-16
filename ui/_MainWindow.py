from PyQt5.QtWidgets import * # type: ignore
from src import AppData
from . import LoginWindow

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        data: AppData = AppData()
        
        if len(data.users) > 0:
            return
        
        window = LoginWindow(self)
        