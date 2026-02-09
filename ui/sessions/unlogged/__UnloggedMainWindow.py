from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import QWidget
from src import AppData
from . import (
    WindowWrapper,
    LogInContainer,
    SignInContainer
)

class UnloggedMainWindow(WindowWrapper):
    
    def __init__(self, parent=None, *args):
        super().__init__(parent)
        self.resize(500, 500)
        
        central = QWidget()
        self.setCentralWidget(central)
        
        self.actual_window: QWidget = QWidget()
        
        if len(AppData.users) > 0:
            
            self.set_window(SignInContainer())
            
            return
        
        self.set_window(LogInContainer())
        self.actual_window.on_log_user.connect(self._on_sign_up_user) # type: ignore
    
    def set_window(self, widget: QWidget):
        
        if self.actual_window:
            self.actual_window.hide()
            self.actual_window.deleteLater()
        
        self.actual_window = widget
        self.actual_window.setParent(self)
        self.actual_window.resize(self.size())
        self.actual_window.show()
    
    def resizeEvent(self, a0: QResizeEvent | None) -> None:
        
        if not a0:
            return
        
        if self.actual_window:
            self.actual_window.resize(a0.size())
        
        return super().resizeEvent(a0)
    
    def _on_sign_up_user(self, id: int):
        
        self.set_window(SignInContainer())
        self.actual_window