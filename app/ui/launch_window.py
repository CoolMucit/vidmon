from PyQt5.QtWidgets import (QMainWindow, QLineEdit, QComboBox, QMessageBox,
                            QPushButton, QStackedWidget, QListWidget)
from PyQt5 import uic
import os

from app.profiles.profile_manager import ProfileManager
from app.ui.main_window import MainWindow
from app.ui.widgets.dialog_widgets.profile_settings_dialog_widget import ProfileSettingsDialogWidget

from app.common.signals.signal_handlers.launch_window_signal_handlers import LaunchWindowSignalHandlers
from app.common.signals.signals import signals

class LaunchWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.profileManager = ProfileManager()
        self.signal_handlers = LaunchWindowSignalHandlers(self)

        self.load_UI()
        self.find_UI_elements()
        self.load_styles()
        self.load_profiles()
        self.setup_signals()

    def load_UI(self):
        ui_path = os.path.join(os.path.dirname(__file__), "interfaces", "launch_window_interface.ui")
        uic.loadUi(ui_path, self)

    def find_UI_elements(self):
        self.profileSelectorCombo: QComboBox = self.findChild(QComboBox, "profileSelectorCombo")
        self.profileSettingsButton: QPushButton = self.findChild(QPushButton, "profileSettingsButton")
        self.createProjectButton: QPushButton = self.findChild(QPushButton, "createProjectButton")
        self.myProjectList: QStackedWidget = self.findChild(QStackedWidget, "myProjectList")

    def load_styles(self):
        style_path = os.path.join("app", "assets", "styles", "launch_window.qss")
        with open(style_path, "r") as file:
            style = file.read()
            self.setStyleSheet(style)

    def load_profiles(self):
        self.profileSelectorCombo.clear()
        profiles = self.profileManager.list_profiles()
        self.profileSelectorCombo.addItems(profiles)

    def setup_signals(self):
        self.createProjectButton.clicked.connect(lambda: signals.createProjectButton_clicked.emit(self))
        self.profileSettingsButton.clicked.connect(lambda: signals.profileSettingsButton_clicked.emit(self))

    def open_profile_settings_dialog(self):
        self.dialog = ProfileSettingsDialogWidget(parent=self)
        self.dialog.exec_() 

    def open_MainWindow(self):
        username = self.profileSelectorCombo.currentText().strip()

        if not username:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir profil seçin.")
            return
        
        self.newProjectWindow = MainWindow(username=username)
        self.newProjectWindow.show()
        print(f"Yeni proje penceresi açıldı: {username}")
        self.close()










