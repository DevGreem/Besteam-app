
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QScrollArea,
    QStyle
)
from PyQt6.QtCore import (
    Qt
)
from src import Signal
from src.steam import SteamClient
from src.steam.models.games import OwnedGameInfo
from ui.components import QUrlImage
from typing import cast
import logging

class GameMiniCard(QWidget):
    clicked: Signal[int] = Signal.create(int)
    _selected_card: "GameMiniCard|None" = None
    
    def __init__(self, game_info: OwnedGameInfo, parent: QWidget) -> None:
        super().__init__(parent)
        self.setFixedHeight(64)
        self.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Expanding
        )
        
        self.info_layout = QHBoxLayout()
        
        logging.debug(f"Loading game info from game {game_info.appid}...")
        self.__load_info(game_info)
        
        self.info_layout.addWidget(self.icon)
        self.info_layout.addWidget(self.name)
        
        self.setLayout(self.info_layout)
        
        logging.debug(f"Loaded game {game_info.appid}")
    
    def __load_info(self, game_info: OwnedGameInfo):
        
        self.info = game_info
        
        steam = SteamClient()
        
        icon_url = steam.apps.get_app_icon(str(game_info.appid), game_info.img_icon_url)
        
        self.icon = QUrlImage(self)
        self.icon.setMaximumSize(64, 64)
        self.icon.set_image(icon_url)
        
        logging.debug("Loaded game icon")
        
        self.name = QLabel(game_info.name)
        self.name.setWordWrap(True)
        self.name.setMaximumWidth(self.maximumWidth())
        
        logging.debug("Loaded game name")
        self.adjustSize()
        
    def parentWidget(self) -> QWidget:
        return super().parentWidget() #type: ignore
    
    def mousePressEvent(self, a0: QMouseEvent | None) -> None:
        
        if not a0:
            return
        
        if a0.button() != Qt.MouseButton.LeftButton:
            return
        
        if GameMiniCard._selected_card and GameMiniCard._selected_card is not self:
            GameMiniCard._selected_card.setStyleSheet("")
        
        GameMiniCard._selected_card = self
        self.clicked.emit(self.info.appid)
        self.__pressed_style()
        
        return super().mousePressEvent(a0)

    def __pressed_style(self):
        
        parent = self.parentWidget()
        
        if isinstance(parent, QScrollArea):
            parent = cast(QWidget, parent.viewport())
        
        bg_color = parent.palette().color(parent.backgroundRole())
        
        logging.debug(f"Parent colors: {bg_color.getRgb()}")
        
        hl_color = bg_color.lighter(135)
        
        logging.debug(f"New Mini Card Color: {hl_color.getRgb()}")
        
        rgba = f"rgba({', '.join(map(lambda color: str(color), hl_color.getRgb()))})"
        self.setStyleSheet(f'background-color: {rgba};')