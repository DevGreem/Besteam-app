from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import * # type: ignore
from PyQt6.QtCore import Qt, pyqtSignal
from typing import cast
from src import (
    AppData,
    UserData,
    Signal
)

class LogInContainer(QWidget):
    
    on_log_user: Signal[int] = cast(Signal[int], pyqtSignal(int))
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        self.login_layout: QVBoxLayout = QVBoxLayout(self)
        self.login_title: QLabel = QLabel("Put your steam ID", self)
        self.login_title.setObjectName("loginTitleLabel")
        
        self.user_id: QLineEdit = QLineEdit(self)
        self.user_id.setObjectName("userIdInput")
        self.user_id.setGeometry(100, 25, 100, 25)
        
        self.submit_user: QPushButton = QPushButton(self)
        self.submit_user.setMaximumSize(100, 25)
        self.submit_user.setText("Log User")
        self.submit_user.clicked.connect(self.on_submit_user)

        self.login_layout.addWidget(self.login_title, Qt.AlignmentFlag.AlignCenter)
        self.login_layout.addWidget(self.user_id, alignment=Qt.AlignmentFlag.AlignCenter)
        self.login_layout.addWidget(self.submit_user, alignment=Qt.AlignmentFlag.AlignCenter)
        self.login_layout.setSpacing(0)
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(self.login_layout)

    def on_submit_user(self, *args):
        
        user_id: int = int(self.user_id.text()) 
        
        AppData.users.add_model(
            UserData(
                id=user_id,
                default_login=False
            )
        )
        
        AppData.save()
        
        self.on_log_user.emit(user_id)