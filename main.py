import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from dotenv import load_dotenv
from ui import AppController
import logging

load_dotenv()

if __name__ == "__main__":
    APP: QApplication = QApplication(sys.argv)
    ICON: QIcon = QIcon('icon.png')
    APP.setWindowIcon(ICON)
    
    logging.basicConfig(level=logging.DEBUG)
    controller = AppController()

    sys.exit(APP.exec())