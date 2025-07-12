from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import QRectF, Qt


class TimelineRuler(QGraphicsItem):
    def __init__(self, scaleFactor: float, startTime: float, duration: float, trackHeaderWidth: int, fps: int = 30, parent=None):
        """
        :param scaleFactor: Piksel başına saniye oranı
        :param startTime: Cetvelin başlangıç zamanı (saniye cinsinden)
        :param duration: Cetvelin toplam süresi (saniye cinsinden)
        :param trackHeaderWidth: Track header genişliği (piksel)
        :param fps: Frame per second (saniyedeki kare sayısı)
        """
        super().__init__(parent)

        self.scaleFactor = scaleFactor
        self.startTime = startTime
        self.duration = duration
        self.trackHeaderWidth = trackHeaderWidth
        self.fps = fps
        self.rulerHeight = 25  # Cetvel yüksekliği

    def boundingRect(self) -> QRectF:
        """
        Cetvelin kapsadığı dikdörtgen alan.
        """
        width = self.duration * self.scaleFactor + self.trackHeaderWidth
        return QRectF(0, 0, width, self.rulerHeight)

    def paint(self, painter: QPainter, option, widget=None):
        # Kalem ve yazı tipi ayarları
        pen = QPen(Qt.black, 1)
        painter.setPen(pen)
        font = QFont("Courier", 8)
        painter.setFont(font)

        # Çizgi uzunlukları
        long_tick_length = int(self.rulerHeight * 0.5)   # Uzun çizgi: cetvel yüksekliğinin %50’si
        short_tick_length = int(self.rulerHeight * 0.25) # Kısa çizgi: cetvel yüksekliğinin %25’i

        # Çizgileri çiz
        for t in range(int(self.startTime), int(self.startTime + self.duration)):
            x = self.trackHeaderWidth + (t - self.startTime) * self.scaleFactor

            if t % 5 == 0:  # Her 5 saniyede bir uzun çizgi ve zaman etiketi
                # Uzun çizgi (aşağıdan yukarı)
                painter.drawLine(
                    int(x), int(self.rulerHeight),       # Başlangıç: cetvelin alt kenarı
                    int(x), int(self.rulerHeight - long_tick_length)  # Bitiş: yukarıya doğru
                )

                # Zaman etiketi (uzun çizginin hemen üstünde)
                text_y = int(self.rulerHeight - long_tick_length - 2)  # 2px yukarı kaydır
                painter.drawText(int(x + 2), text_y, self.format_time(t))
            else:  # Kısa çizgi
                painter.drawLine(
                    int(x), int(self.rulerHeight),       # Başlangıç: cetvelin alt kenarı
                    int(x), int(self.rulerHeight - short_tick_length)  # Bitiş: yukarıya doğru
                )

    def format_time(self, total_seconds: float) -> str:
        """
        Toplam saniyeyi Saat:Dakika:Saniye:Frame formatına dönüştürür.
        """
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        frames = int((total_seconds - int(total_seconds)) * self.fps)
        return f"{hours:02}:{minutes:02}:{seconds:02}.{frames:02}"

    def set_scale_factor(self, newScaleFactor: float):
        """
        Ölçek faktörünü değiştirir ve cetveli günceller.
        """
        print(f"[Ruler] Scale factor güncellendi: {newScaleFactor}")
        self.scaleFactor = newScaleFactor
        self.prepareGeometryChange()
        self.update()
