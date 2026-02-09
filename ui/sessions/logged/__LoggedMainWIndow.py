from PyQt6.QtGui import (
    QResizeEvent
)
from PyQt6.QtCore import (
    Qt
)
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QSizePolicy
)
from . import (
    WindowWrapper
)
from ui.components.menu import TwoSideMenu
from ui.components.library import GamesLibrary
import logging

class LoggedMainWindow(WindowWrapper):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        central = QWidget()
        self.setCentralWidget(central)
        
        self.right_layout = QVBoxLayout(central)
        
        self.__load_sections()
    
    def __load_sections(self):
                
        self.menu = TwoSideMenu(self.centralWidget())
        
        self.content = GamesLibrary(self.centralWidget())
        self.content.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        
        self.right_layout.addWidget(self.menu)
        self.right_layout.addWidget(self.content)
    
    def resizeEvent(self, a0: QResizeEvent | None) -> None:
        super().resizeEvent(a0)
        
        logging.debug(a0.size()) # type: ignore