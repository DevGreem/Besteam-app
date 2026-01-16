from PyQt5.QtWidgets import QMainWindow
from src import StylesManager

class WindowWrapper(QMainWindow):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        self.setStyleSheet('styles/global.css')
        self.setWindowTitle("Besteam")
        self.setFixedSize(500, 500)
        
        StylesManager.load_style_file("ui/styles/global.css", self)