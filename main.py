import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtCore import * # type: ignore
from PyQt5.QtGui import * # type: ignore
from dotenv import load_dotenv
from ui import MainWindow

load_dotenv()


if __name__ == "__main__":
    APP: QApplication = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()

    APP.exec()