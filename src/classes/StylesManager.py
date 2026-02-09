from pathlib import Path
from PyQt6.QtWidgets import QMainWindow
from src.utils import resource_path

def load_style_file(style_path: str|Path, window: QMainWindow):
    
    with open(resource_path(style_path), "r") as style:
        window.setStyleSheet(style.read())