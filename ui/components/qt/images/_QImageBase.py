from PyQt6.QtGui import QPaintEvent, QPainter, QPixmap
from PyQt6.QtWidgets import QWidget

class QImageBase(QWidget):
    
    pixmap: QPixmap
    
    def __init__(self, auto_load: bool = False, path: str = "", parent: QWidget | None = None):
        super().__init__(parent)
        self.pixmap = QPixmap()
        
        if auto_load:
            self.set_image(path)
    
    def set_image(self, path: str):
        raise NotImplementedError("Subclasses must implement set_image")
    
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)