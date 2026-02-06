from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QSizePolicy
)
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtCore import QObject
from src import Logger
from typing import cast

class TwoSideMenu(QWidget):
    
    def __init__(self, parent: QWidget|None=None):
        super().__init__(parent=parent)
        self.show()
        
        self.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Fixed
        )
        
        self.setFixedHeight(36)
        
        if parent:
            parent_size = parent.window().size() # type: ignore
            
            Logger.log(parent_size)
            self.setFixedWidth(parent_size.width())
        
        self.widgets_layout = QHBoxLayout(self)
        
        home = QPushButton("Besteam")
        
        self.widgets_layout.addWidget(home)
        
        self.widgets_layout.addStretch()
        
        profile = QPushButton("Profile")
        
        self.widgets_layout.addWidget(profile)

        self.setLayout(self.widgets_layout)