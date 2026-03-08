from . import QImageBase
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap
from pathlib import Path

class QImage(QImageBase):
    
    def __init__(self, auto_load: bool = False, image_path: str|Path = "", parent: QWidget | None = None):
        super().__init__(auto_load, str(image_path), parent)
    
    def set_image(self, image_path: str|Path): # type: ignore
        
        path = str(image_path)
        self.pixmap.load(path)