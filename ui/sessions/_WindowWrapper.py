from PyQt6.QtWidgets import QMainWindow
from src import StylesManager
import logging

class WindowWrapper(QMainWindow):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        self.setWindowTitle("Besteam")
        self.resize(500, 500)
        logging.debug(f"Opened {self.__class__.__name__}")
        
        StylesManager.load_style_file("ui/global.css", self)