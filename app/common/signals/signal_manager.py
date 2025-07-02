from PyQt5.QtCore import QObject, pyqtSignal

#### SİNYAL TANIMLAMA SINIFI ####

class SignalManager(QObject):

    #! Signals for Launch Window
    createProjectButton_clicked = pyqtSignal(object)  # yeni proje penceresi açıldı
    main_window_closed = pyqtSignal()  # ana pencere kapatıldı

    profileSettingsButton_clicked = pyqtSignal(object)  # profil ayarları penceresi açıldı
    # Signals for Profile Settings Dialog


    confirmProfileButton_clicked = pyqtSignal()  # profil değişiklikleri onaylandı

    #! Signals for Main Window



    def __init__(self):
        super().__init__()
