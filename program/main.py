import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


# Ana pencere sınıfımız
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # QMainWindow sınıfını başlat
        self.setWindowTitle("Vidmon")  # Pencere başlığı
        self.setGeometry(100, 100, 800, 600)  # x, y, genişlik, yükseklik


# Uygulama başlatıcı kod
if __name__ == "__main__":
    app = QApplication(sys.argv)  # PyQt uygulamasını başlat
    window = MainWindow()         # Pencere nesnesi oluştur
    window.show()                 # Pencereyi göster
    sys.exit(app.exec_())         # Olay döngüsünü başlat
