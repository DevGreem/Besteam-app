from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QSizePolicy
)
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
import logging

class TwoSideMenu(QWidget):
    
    def __init__(self, parent: QWidget|None=None):
        super().__init__(parent=parent)
        self.show()
        
        self.setFixedHeight(48)
        self.setMaximumHeight(48)
        
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )
        
        self.widgets_layout = QHBoxLayout(self)
        
        self.__load_buttons()
    
    def __load_buttons(self):
        
        home = QPushButton("Besteam")
        home.setIcon(QIcon("icon.png"))
        home.setIconSize(QSize(24, 24))
        
        self.widgets_layout.addWidget(home)
        
        self.widgets_layout.addStretch()
        
        profile = QPushButton("Profile")
        
        self.widgets_layout.addWidget(profile)

        self.setLayout(self.widgets_layout)