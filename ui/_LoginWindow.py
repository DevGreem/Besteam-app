from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import * # type: ignore
from PyQt6.QtCore import Qt, QSize
from src import AppData, Window

class LoginWindow(Window):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        self.login_layout: QVBoxLayout = QVBoxLayout(self)
        self.login_title: QLabel = QLabel("Put your steam ID", self)
        self.login_title.setObjectName("loginTitleLabel")
        
        self.user_id: QPlainTextEdit = QPlainTextEdit(self)
        self.user_id.setObjectName("userIdInput")
        self.user_id.setMaximumHeight(100)
        self.user_id.setMaximumWidth(300)

        self.login_layout.addWidget(self.login_title)
        self.login_layout.addWidget(self.user_id)
        self.login_layout.setAlignment(self.login_title, Qt.AlignmentFlag.AlignCenter)
        self.login_layout.setAlignment(self.user_id, Qt.AlignmentFlag.AlignCenter)
        self.login_layout.setSpacing(0)
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(self.login_layout)
