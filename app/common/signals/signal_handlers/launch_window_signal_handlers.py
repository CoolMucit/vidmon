from app.common.signals.signals import signals

class LaunchWindowSignalHandlers:
    def __init__(self, launch_window):

        self.launch_window = launch_window

        self.connect_signals()

    def connect_signals(self):

        signals.createProjectButton_clicked.connect(self.launch_window.open_MainWindow) # Yeni proje penceresini açar ve LaunchWindow'u kapatır
        signals.main_window_closed.connect(self.launch_window.show) # MainWindow kapatıldığında LaunchWindow'u açar

        signals.profileSettingsButton_clicked.connect(self.launch_window.open_profile_settings_dialog) # Profil ayarları penceresini açar

        signals.confirmProfileButton_clicked.connect(self.launch_window.load_profiles) # Profil değişikliklerini onaylar