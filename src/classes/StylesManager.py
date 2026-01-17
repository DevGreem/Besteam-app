from pathlib import Path
from PyQt6.QtWidgets import QMainWindow

def load_style_file(style_path: str|Path, window: QMainWindow):
        
    with open(style_path, "r") as style:
        window.setStyleSheet(style.read())