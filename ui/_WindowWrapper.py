from PyQt6.QtWidgets import QMainWindow
from src import StylesManager

class WindowWrapper(QMainWindow):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        self.setWindowTitle("Besteam")
        self.resize(500, 500)
        
        StylesManager.load_style_file("ui/global.css", self)