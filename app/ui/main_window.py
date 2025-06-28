from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from app.ui.widgets.media_panel_widget import MediaPanel
from PyQt5.QtCore import Qt
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app/ui/interfaces/main_window_interface.ui", self)
        self.showMaximized() 

        # Sekme konumunu değiştirmek için:
        self.setTabPosition(Qt.TopDockWidgetArea, QTabWidget.North)
        self.setTabPosition(Qt.BottomDockWidgetArea, QTabWidget.North)
        self.setTabPosition(Qt.LeftDockWidgetArea, QTabWidget.North)
        self.setTabPosition(Qt.RightDockWidgetArea, QTabWidget.North)

        # medya paneli ayarları
        self.media_panel = MediaPanel(
            media_panel_widget=self.mediaPanel
        )

        # STYLE qss
        style_path = os.path.join("app", "assets", "styles", "main_window.qss")
        with open(style_path, "r") as file:
            style = file.read()
            self.setStyleSheet(style)

