from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import os

from app.common.constants.global_constants import APP_NAME

from app.profiles.user_profile import UserProfile

from app.common.signals.signals import signals

class MainWindow(QMainWindow):

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
        self.setWindowTitle(APP_NAME + f" ({username})")
        self.showMaximized()

    def closeEvent(self, event):
        signals.main_window_closed.emit()
        super().closeEvent(event)
