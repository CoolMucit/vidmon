from PyQt5.QtWidgets import (QMainWindow, QLineEdit, QComboBox, QMessageBox, 
                            QPushButton, QStackedWidget, QListWidget)
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import os

from app.ui.main_window import MainWindow
from app.profiles.profile_manager import ProfileManager

class LaunchWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.profileManager = ProfileManager()

        self.load_UI()
        self.find_UI_elements()
        self.load_styles()
        self.load_profiles()
        self.setup_signals()

    def load_UI(self):
        ui_path = os.path.join(os.path.dirname(__file__), "interfaces", "launch_window_interface.ui")
        uic.loadUi(ui_path, self)

    def find_UI_elements(self):
        self.profileCombo: QComboBox = self.findChild(QComboBox, "profileCombo")
        self.profileButton: QPushButton = self.findChild(QPushButton, "profileButton")
        self.startButton: QPushButton = self.findChild(QPushButton, "startButton")
        self.stack: QStackedWidget = self.findChild(QStackedWidget, "controlsLaunchWidget")  # tüm sayfaları yöneten
        self.profileLine: QLineEdit = self.findChild(QLineEdit, "profileLine")
        self.createProfileButton: QPushButton = self.findChild(QPushButton, "createProfileButton")
        self.profileList: QListWidget = self.findChild(QListWidget, "profileList")

    def load_styles(self):
        style_path = os.path.join("app", "assets", "styles", "launch_window.qss")
        with open(style_path, "r") as file:
            style = file.read()
            self.setStyleSheet(style)

    def load_profiles(self):
        self.profileCombo.clear()
        profiles = self.profileManager.list_profiles()
        self.profileCombo.addItems(profiles)
        self.profileList.addItems(profiles)

    def setup_signals(self):
        self.profileButton.clicked.connect(self.show_profile_page)
        self.createProfileButton.clicked.connect(self.create_profile)
        self.startButton.clicked.connect(self.open_MainWindow)

    @pyqtSlot()
    def show_profile_page(self):
        self.stack.setCurrentIndex(3)  # profil oluşturma sayfasına geç

    @pyqtSlot()
    def create_profile(self):
        username = self.profileLine.text().strip()

        if not username:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı boş olamaz.")
            return

        if self.profileManager.profile_exists(username):
            QMessageBox.warning(self, "Uyarı", "Bu kullanıcı zaten var.")
            return

        self.profileManager.create_profile(username)
        self.load_profiles()

        # Geri ana sayfaya dön
        self.stack.setCurrentIndex(0)
        self.profileLine.clear()

    @pyqtSlot()
    def open_MainWindow(self):
        username = self.profileCombo.currentText().strip()
        if not username:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir profil seçin.")
            return

        self.newProjectWindow = MainWindow(username=username)
        self.newProjectWindow.closed.connect(self.show_LaunchWindow)
        self.newProjectWindow.show()
        self.hide()

    def show_LaunchWindow(self):
        self.show()
