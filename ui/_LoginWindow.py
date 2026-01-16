from PyQt5.QtWidgets import * # type: ignore
from src import AppData

class LoginWindow(QWidget):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        self.login_title: QLabel = QLabel("Put your steam ID", self)
        self.login_title.setObjectName("loginTitleLabel")
        
        self.login_title.move(
            int(self.size().width()/2),
            int(self.size().height()/2)
        )