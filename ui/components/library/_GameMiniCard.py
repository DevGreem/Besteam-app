
from PyQt6.QtGui import QMouseEvent
from ui.components import UrlImageLabel
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QSizePolicy
)
from PyQt6.QtCore import (
    pyqtSignal,
    Qt
)
from typing import cast
from src.steam import SteamClient
from src.steam.models.games import OwnedGameInfo
from src import Signal
import logging

class GameMiniCard(QWidget):
    clicked: Signal[int] = cast(Signal[int], pyqtSignal(int))
    
    def __init__(self, game_info: OwnedGameInfo, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setFixedHeight(64)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )
        
        self.info_layout = QHBoxLayout()
        
        self.__load_info(game_info)
        
        self.info_layout.addWidget(self.icon)
        self.info_layout.addWidget(self.name)
        
        self.setLayout(self.info_layout)
        
        logging.debug(f"Loaded game {game_info.appid}")
    
    def __load_info(self, game_info: OwnedGameInfo):
        
        self.info = game_info
        
        steam = SteamClient()
        icon_url = steam.apps.get_app_icon(str(game_info.appid), game_info.img_icon_url)
        
        self.icon = UrlImageLabel(icon_url)
        self.icon.setMaximumSize(64, 64)
        self.icon.resize(64, 64)
        
        self.name = QLabel(game_info.name)
        self.name.setMaximumHeight(self.maximumHeight())
    
    def mousePressEvent(self, a0: QMouseEvent | None) -> None:
        
        if not a0:
            return
        
        if a0.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.info.appid)
        
        return super().mousePressEvent(a0)