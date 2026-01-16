from PyQt5.QtWidgets import * # type: ignore

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        
        self.setMinimumSize(500, 500)
        self.setWindowTitle("Besteam")
        
        login_title: QLabel = QLabel("Put your steam ID", self)
        