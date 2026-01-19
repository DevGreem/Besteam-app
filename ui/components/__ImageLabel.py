from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QUrl, Qt
from typing import overload, Optional

class ImageLabel(QLabel):
    
    def __init__(self, path: str, parent=None):
        super().__init__(parent)
        self.image: QPixmap = QPixmap(path)
        self.setPixmap(self.image)

    def scalePixmap(self,
        width: int,
        height: int,
        aspectRatioMode: Qt.AspectRatioMode = Qt.AspectRatioMode.KeepAspectRatio,
        transformMode: Qt.TransformationMode = Qt.TransformationMode.SmoothTransformation
    ):
        
        self.setPixmap(self.pixmap().scaled(width, height, aspectRatioMode, transformMode))