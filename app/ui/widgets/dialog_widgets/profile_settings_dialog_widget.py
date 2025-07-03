from PyQt5.QtWidgets import QDialog, QListWidget, QPushButton, QInputDialog, QMessageBox
from PyQt5 import uic

from app.profiles.profile_manager import ProfileManager
from app.profiles.user_profile import UserProfile

from app.common.signals.signals import signals

class ProfileSettingsDialogWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.profile_manager = ProfileManager()
        self.temporary_profiles = self.profile_manager.list_profiles()[:]

        self.load_UI()
        self.find_UI_elements()
        self.load_profiles()
        self.load_options()
        self.setup_signals()


    def load_UI(self):
        uic.loadUi("app/ui/interfaces/dialog_interfaces/profile_settings_dialog_interface.ui", self)

    def find_UI_elements(self):
        self.profileList: QListWidget = self.findChild(QListWidget, "profileList")
        self.createProfileButton: QPushButton = self.findChild(QPushButton, "createProfileButton")
        self.editProfileButton: QPushButton = self.findChild(QPushButton, "editProfileButton")
        self.deleteProfileButton: QPushButton = self.findChild(QPushButton, "deleteProfileButton")
        self.importProfileButton: QPushButton = self.findChild(QPushButton, "importProfileButton")
        self.exportProfileButton: QPushButton = self.findChild(QPushButton, "exportProfileButton")
        self.confirmProfileButton: QPushButton = self.findChild(QPushButton, "confirmProfileButton")
        self.cancelProfileButton: QPushButton = self.findChild(QPushButton, "cancelProfileButton")

    def load_profiles(self):
        self.profileList.clear()
        profiles = ProfileManager().list_profiles()
        self.profileList.addItems(profiles)

    def load_options(self):
        self.setWindowTitle("Profil Ayarları")

    def setup_signals(self):
        self.createProfileButton.clicked.connect(self.create_profile)  # Yeni profil oluşturma butonu tıklandı
        self.editProfileButton.clicked.connect(self.edit_profile)
        self.deleteProfileButton.clicked.connect(self.delete_profile)
        self.confirmProfileButton.clicked.connect(self.confirm_changes)
        self.cancelProfileButton.clicked.connect(self.cancel_changes)

    def create_profile(self):
        new_name, ok = QInputDialog.getText(
            self,
            "Yeni Profil",
            "Yeni profil ismi:"
        )

        if ok and new_name.strip():
            new_name = new_name.strip()

            if new_name in self.temporary_profiles:
                QMessageBox.information(self, "Uyarı", "Bu isim zaten var.")
                return

            self.temporary_profiles.append(new_name)
            self.profileList.addItem(new_name)

    def edit_profile(self):
        item = self.profileList.currentItem()

        if item:
            old_name = item.text()

            new_name, ok = QInputDialog.getText(
                self,
                "Profil Düzenle",
                "Yeni profil ismi:",
                text=old_name
            )

            if ok and new_name.strip():
                new_name = new_name.strip()

                if new_name in self.temporary_profiles and new_name != old_name:
                    self.show_message("Uyarı", "Bu isim zaten var.")
                    return

                index = self.temporary_profiles.index(old_name)
                self.temporary_profiles[index] = new_name
                item.setText(new_name)

    def delete_profile(self):
        item = self.profileList.currentItem()

        if item:
            name = item.text()

            if name in self.temporary_profiles:
                index = self.temporary_profiles.index(name)
                self.temporary_profiles.pop(index)

            self.profileList.takeItem(self.profileList.row(item))

    def confirm_changes(self):
        # Önceki profilleri sil
        for existing in self.profile_manager.list_profiles():
            self.profile_manager.delete_profile(existing)

        # Geçici listedekileri oluştur
        for name in self.temporary_profiles:
            self.profile_manager.create_profile(name)

        signals.confirmProfileButton_clicked.emit()  # Profil değişikliklerini onaylar
        QMessageBox.information(self, "Başarılı", "Profil değişiklikleri kaydedildi.")
        self.close()

    def cancel_changes(self):
        self.close()  # Pencereyi kapat










