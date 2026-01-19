from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from src import ImageLabel, Signal
from src.steam import Player
from typing import cast

class UserBigCard(QWidget):
    
    clicked: Signal[Player] = cast(Signal[Player], pyqtSignal(Player))
    
    def __init__(self, user: Player, parent: QWidget | None = None, width: int = 300, height: int = 300) -> None:
        super().__init__(parent)
        self.resize(width, height)
        self.user = user
        
        self.user_layout = QVBoxLayout(self)
        self.user_layout.setContentsMargins(0, 0, 0, 0)
        self.user_layout.setSpacing(0)
        
        self.avatar = ImageLabel(user.avatarfull, self)
        self.username = QLabel(user.personaname, self)
        
        self.user_layout.addWidget(self.avatar, 0, Qt.AlignmentFlag.AlignHCenter)
        self.user_layout.addWidget(self.username, 0, Qt.AlignmentFlag.AlignTop)
        self.username.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.setLayout(self.user_layout)
    
    def mousePressEvent(self, a0: QMouseEvent | None) -> None:
        self.clicked.emit(self.user)
        return super().mousePressEvent(a0)