# from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsTextItem
# from PyQt5.QtCore import QRectF, Qt
# from PyQt5.QtGui import QColor, QBrush, QPen

# class TimelineClip(QGraphicsRectItem):
#     """
#     Zaman çizelgesindeki bir medya klibini temsil eden QGraphicsItem.
#     """
#     def __init__(self, name: str, start_time: float, duration: float, track_index: int, parent=None):
#         # Dikdörtgenin boyutları ve konumu: (x, y, genişlik, yükseklik)
#         # x: zaman çizelgesindeki başlangıç zamanına göre konum
#         # y: hangi track'te olduğuna göre dikey konum (şimdilik basit bir çarpan kullanacağız)
#         # genişlik: süresine göre uzunluk
#         # yükseklik: klip yüksekliği
        
#         self.clip_height = 40  # Kliplerin sabit yüksekliği
#         self.time_to_pixel_scale = 20 # 1 saniye kaç piksel olsun (ölçeklendirme için)
        
#         x = start_time * self.time_to_pixel_scale
#         y = track_index * (self.clip_height + 10) # Track'ler arası boşluk için 10 piksel ekledik
#         width = duration * self.time_to_pixel_scale
#         height = self.clip_height

#         super().__init__(QRectF(x, y, width, height), parent)

#         self.name = name
#         self.start_time = start_time
#         self.duration = duration
#         self.track_index = track_index # Hangi track'e ait olduğunu belirtir

#         self.setBrush(QBrush(QColor("#1abc9c"))) # Klip rengi
#         self.setPen(QPen(QColor("#16a085"), 1)) # Klip kenarlık rengi

#         # Klip adını göstermek için metin öğesi
#         self.text_item = QGraphicsTextItem(self.name, self)
#         # Metni klipin içine ortalayalım (basit bir yaklaştırma)
#         self.text_item.setDefaultTextColor(Qt.white)
#         text_rect = self.text_item.boundingRect()
#         self.text_item.setPos(x + (width - text_rect.width()) / 2, y + (height - text_rect.height()) / 2)

#     def get_start_time(self) -> float:
#         return self.start_time

#     def get_duration(self) -> float:
#         return self.duration

#     def get_track_index(self) -> int:
#         return self.track_index

#     # Klipin konumunu ve boyutunu güncelleyen bir metot (ölçek veya zaman değiştiğinde kullanılabilir)
#     def update_geometry(self, time_to_pixel_scale: float, track_y_offset: float):
#         self.time_to_pixel_scale = time_to_pixel_scale
#         x = self.start_time * self.time_to_pixel_scale
#         y = track_y_offset # Bu Y değeri dışarıdan belirlenecek
#         width = self.duration * self.time_to_pixel_scale
        
#         self.setRect(QRectF(x, y, width, self.clip_height))
#         # Metin konumunu da güncelle
#         text_rect = self.text_item.boundingRect()
#         self.text_item.setPos(x + (width - text_rect.width()) / 2, y + (self.clip_height - text_rect.height()) / 2)















