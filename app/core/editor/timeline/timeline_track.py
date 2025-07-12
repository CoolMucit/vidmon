from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt


class TimelineTrack(QGraphicsRectItem):
    def __init__(self, x, y, width, height, track_name="Yeni Track", track_index=0, header_width=100):
        super().__init__(x, y, width, height)
        """
        x, y           : Track'in sahnedeki konumu
        width, height  : Track toplam boyutu
        track_name     : Track başlığı
        track_index    : Track'in sahnedeki sırası
        header_width   : Başlık kısmının genişliği
        color          : Track arka plan rengi
        """

        # Track temel özellikleri
        self.track_name = track_name
        self.track_index = track_index  # Kliplerin sahnedeki Y konumunu belirleyecek
        self.clip_list = []  # TimelineClip nesnelerinin listesi
        self.is_locked = False
        self.is_visible = True

        # Genel track arka plan rengi
        self.setBrush(QBrush(Qt.lightGray))

        # Track başlığı (sol kısım)
        self.track_header = QGraphicsRectItem(0, 0, header_width, height, parent=self)
        self.track_header.setBrush(QBrush(Qt.darkGray))  # Başlık için koyu gri
        self.track_header.setPos(x, y)

        # Track içeriği (sağ kısım)
        self.track_content = QGraphicsRectItem(0, 0, width - header_width, height, parent=self)
        self.track_content.setBrush(QBrush(Qt.gray))  # İçerik için normal gri
        self.track_content.setPos(x + header_width, y)

        # Taşınamaz ve seçilemez
        self.setFlag(QGraphicsRectItem.ItemIsMovable, False)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable, False)

    #! Getter / Setter Metodları
    def get_track_name(self) -> str:
        return self.track_name

    def set_track_name(self, new_track_name: str):
        old_track_name = self.track_name
        self.track_name = new_track_name
        print(f"'{old_track_name}' parçasının ismi '{new_track_name}' olarak değiştirildi.")

    def get_track_index(self) -> int:
        return self.track_index


        
    # def add_clip(self, clip: TimelineClip):
    #     """Parçaya bir TimelineClip nesnesi ekler."""
    #     if isinstance(clip, TimelineClip):
    #         self.clips.append(clip)
    #         # Klipin track_index'ini ayarlayalım
    #         clip.track_index = self.track_index
    #         print(f"'{clip.name}' klibi '{self.track_name}' (ID: {self.track_index}) parçasına eklendi.")
    #     else:
    #         print("Hata: Sadece TimelineClip nesneleri eklenebilir.")

    # def remove_clip(self, clip_id: str):
    #     """Belirtilen ID'ye sahip klibi parçadan kaldırır."""
    #     # Burada klip ID'ye göre kaldırma mantığı eklenecek
    #     # Basitlik için şimdilik sadece referansa göre kaldırma yapalım
    #     for clip in list(self.clips): # Kopyası üzerinde döngü yap, silerken hata almamak için
    #         if clip.name == clip_id: # Farazi olarak klip adını ID gibi kullandık
    #             self.clips.remove(clip)
    #             print(f"'{clip_id}' klibi '{self.track_name}' parçasından kaldırıldı.")
    #             return True
    #     return False

    # def get_clips(self) -> list:
    #     """Bu parçadaki tüm TimelineClip nesnelerinin bir listesini döndürür."""
    #     return self.clips

    # def is_track_locked(self) -> bool:
    #     return self.is_locked

    # def change_lock_status(self, lock_status: bool):
    #     self.is_locked = lock_status
    #     print(f"'{self.track_name}' parçası kilit durumu: {self.is_locked}")

    # def is_track_visible(self) -> bool:
    #     return self.is_visible

    # def change_visible_status(self, visible_status: bool):
    #     self.is_visible = visible_status
    #     print(f"'{self.track_name}' parçası görünürlük durumu: {self.is_visible}")
    #     # Bağlı olduğu kliplerin görünürlüğünü de burada ayarlayabiliriz.
    #     for clip in self.clips:
    #         clip.setVisible(visible_status)