import sys
from PyQt5.QtWidgets import QApplication
from dotenv import load_dotenv
from ui import MainWindow

load_dotenv()

if __name__ == "__main__":
    APP: QApplication = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()

    APP.exec()