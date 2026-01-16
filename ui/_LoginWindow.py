from PyQt5.QtWidgets import * # type: ignore
from src import AppData

class LoginWindow(QWidget):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        login_title: QLabel = QLabel("Put your steam ID", self)
        