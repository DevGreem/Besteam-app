from . import QImageBase
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt6.QtCore import QUrl
import requests

class QUrlImage(QImageBase):
    
    def __init__(self, parent: QWidget | None = None):
        super().__init__(False, "", parent)
        
        self.manager = QNetworkAccessManager(self)
        self.manager.finished.connect(self._on_finished)
    
    def set_image(self, url: str): # type: ignore
        
        request = QNetworkRequest(QUrl(url))
        
        self.manager.get(request)
    
    def _on_finished(self, reply: QNetworkReply):
        self.pixmap.loadFromData(reply.readAll())
        
        self.setFixedSize(self.pixmap.size())
        self.adjustSize()