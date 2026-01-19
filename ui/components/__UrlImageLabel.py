from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt6.QtCore import QUrl
from typing import overload, Optional

class UrlImageLabel(QLabel):
    
    @overload
    def __init__(self, url: str): ...
    
    @overload
    def __init__(self, parent: Optional[QWidget] = None): ...
    
    @overload
    def __init__(self, url: str, parent: Optional[QWidget] = None): ...
    
    def __init__(self, url: str, parent: Optional[QWidget] = None): # type: ignore
             
        if not isinstance(url, str):
            parent = url
        
        super().__init__(parent)
        
        self.manager = QNetworkAccessManager(self)
        self.manager.finished.connect(self._on_finished)
        self.setPixmapUrl(url)
        
    
    def setPixmapUrl(self, url: str):
        request = QNetworkRequest(QUrl(url))
        
        self.manager.get(request)

    def _on_finished(self, reply: QNetworkReply):
        pixmap = QPixmap()
        pixmap.loadFromData(reply.readAll())
        
        self.setFixedSize(pixmap.size())
        self.setPixmap(pixmap)
        self.adjustSize()