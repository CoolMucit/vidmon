from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from app.widgets.media_panel import MediaPanel
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app/gui/main_window.ui", self)
        self.showMaximized() 

        # medya paneli ayarları
        self.media_panel = MediaPanel(
            media_panel_widget=self.mediaPanel
        )

        # qss style dosyalarını yükle
        style_path = os.path.join("app", "styles", "main_window.qss")
        with open(style_path, "r") as file:
            style = file.read()
            self.setStyleSheet(style)

