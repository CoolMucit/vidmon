from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
import os

from app.profiles.user_profile import UserProfile

class MainWindow(QMainWindow):
    closed = pyqtSignal()  # Sinyal tanımlama

    def __init__(self, username):
        super().__init__()

        self.username = username

        self.load_UI()
        self.load_styles()
        self.load_user_profile(self.username)
        self.load_options(self.username)

    def load_UI(self):
        uic.loadUi("app/ui/interfaces/main_window_interface.ui", self)

    def load_styles(self):
        style_path = os.path.join("app", "assets", "styles", "main_window.qss")
        with open(style_path, "r") as file:
            style = file.read()
            self.setStyleSheet(style)

    def load_user_profile(self, username):
        self.user_profile = UserProfile(username)
        self.user_profile.load()

    def load_options(self, username):
        self.setWindowTitle(f"Vidmon ({username})")
        # self.showMaximized()

    # KAPATILMA SİNYALİ YAYAR
    def closeEvent(self, event):
        self.closed.emit()  # sinyal yayılır
        super().closeEvent(event)

        

