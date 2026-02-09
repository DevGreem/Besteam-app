from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout
)
import logging
from src import SteamClient

class GamesList(QWidget):
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        steam = SteamClient()
        