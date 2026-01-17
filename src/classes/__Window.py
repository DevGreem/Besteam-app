from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSignal, QSize
from . import Signal
from typing import cast

class Window(QWidget):
    
    on_change_height: Signal[int] = cast(Signal[int], pyqtSignal(int))
    on_change_width: Signal[int] = cast(Signal[int], pyqtSignal(int))
    on_change_size: Signal[QSize] = cast(Signal[QSize], pyqtSignal(QSize))
    
    def setFixedHeight(self, h: int):
        super().setFixedHeight(h)
        self.on_change_height.emit(h)
        self.on_change_size.emit(self.size())
    
    def setFixedWidth(self, w: int):
        super().setFixedWidth(w)
        self.on_change_width.emit(w)
        self.on_change_size.emit(self.size())