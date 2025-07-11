from PyQt5.QtWidgets import (QDockWidget, QGraphicsView, QGraphicsScene, 
                            QGraphicsRectItem, QSlider, QGraphicsLineItem, QGraphicsTextItem)
from PyQt5.QtCore import Qt, QRectF
from PyQt5 import uic

class TimelineEditorDockWidget(QDockWidget):
    def __init__(self):
        super().__init__()

        self.load_UI()
        self.find_UI_elements()


        self.track_height = 100
        self.track_count = 3
        self.timeline_width_seconds = 60  # Varsayılan timeline genişliği (saniye)
        self.pixels_per_second = 100      # 1 saniye = 100px

        # Zaman cetveli ve timeline sahnelerini oluştur
        self.timeline_ruler_scene = QGraphicsScene(self)
        self.timeline_scene = QGraphicsScene(self)

        # QGraphicsView'lere sahneleri ata
        self.timelineRulerGraphicsView.setScene(self.timeline_ruler_scene)
        self.timelineEditorGraphicsView.setScene(self.timeline_scene)

        # Trackları ve zaman çizelgesini çiz
        self.draw_tracks()
        self.draw_time_ruler()

        #! Slider'ı bağla
        self.timelineScaleControlSlider.valueChanged.connect(self.scale_timeline)

        #! Scroll senkronizasyonu
        self.timelineRulerGraphicsView.horizontalScrollBar().valueChanged.connect(
            self.timelineEditorGraphicsView.horizontalScrollBar().setValue
        )
        self.timelineEditorGraphicsView.horizontalScrollBar().valueChanged.connect(
            self.timelineRulerGraphicsView.horizontalScrollBar().setValue
        )






    def load_UI(self):
        uic.loadUi("app/ui/interfaces/dock_interfaces/editor_dock_interfaces/timeline_editor_dock_interface.ui", self)

    def find_UI_elements(self):
        self.timelineEditorGraphicsView: QGraphicsView = self.findChild(QGraphicsView, "timelineEditorGraphicsView")
        self.timelineRulerGraphicsView: QGraphicsView = self.findChild(QGraphicsView, "timelineRulerGraphicsView")
        self.timelineScaleControlSlider: QSlider = self.findChild(QSlider, "timelineScaleControlSlider")




    def draw_tracks(self):
        """
        Timeline üzerindeki trackları çizer.
        """
        total_width = self.timeline_width_seconds * self.pixels_per_second
        colors = [Qt.red, Qt.green, Qt.blue]

        for index in range(self.track_count):
            y_position = index * self.track_height
            rect = QGraphicsRectItem(0, y_position, total_width, self.track_height)
            rect.setBrush(colors[index % len(colors)])
            rect.setZValue(-1)  # Arka plan
            self.timeline_scene.addItem(rect)

        # Scene genişliğini ayarla
        self.timeline_scene.setSceneRect(QRectF(0, 0, total_width, self.track_count * self.track_height))



    def draw_time_ruler(self):
        """
        Zaman cetvelini çizer.
        """
        total_width = self.timeline_width_seconds * self.pixels_per_second
        height = 40  # Zaman cetvelinin yüksekliği
        second_step = 1  # Her saniyede bir çizgi

        for second in range(self.timeline_width_seconds + 1):
            x = second * self.pixels_per_second
            line = QGraphicsLineItem(x, 0, x, height)
            self.timeline_ruler_scene.addItem(line)

            # Zaman etiketi
            label = QGraphicsTextItem(f"{second}s")
            label.setPos(x + 2, height / 2)
            self.timeline_ruler_scene.addItem(label)

        # Scene genişliğini ayarla
        self.timeline_ruler_scene.setSceneRect(QRectF(0, 0, total_width, height))




    #!   # Slider ile timeline ölçeğini değiştirir
    def scale_timeline(self, value):
        scale_factor = value / 50  # Slider'ın orta değeri 50 → 1x zoom

        if scale_factor <= 0:
            scale_factor = 0.1  # Minimum ölçek

        # Yeni ölçeği uygula
        self.timelineRulerGraphicsView.resetTransform()
        self.timelineEditorGraphicsView.resetTransform()

        self.timelineRulerGraphicsView.scale(scale_factor, 1)
        self.timelineEditorGraphicsView.scale(scale_factor, 1)

















#     def add_clip_to_timeline(self, file_path: str, start_time: int, duration: int):
#         clip = Clip(file_path, start_time, duration)
#         self.timeline_container.get_track(0).add_clip(clip)

#         # Timeline’a görsel olarak çiz
#         self.timeline_view.draw_clip(start_time, duration)

#     def draw_playhead(self, position_x: int, timeline_height: int):
#         playhead = QGraphicsRectItem(position_x * self.time_scale, 0, 2, timeline_height)
#         playhead.setBrush(Qt.red)
#         self.timelineEditorGraphicsView.scene.addItem(playhead)

#     def draw_clip(self, start_time: int, duration: int, y_pos: int = 0):
#         x = start_time * self.time_scale
#         width = duration * self.time_scale
#         rect = QGraphicsRectItem(x, y_pos, width, 50)
#         rect.setBrush(Qt.green)
#         self.timelineEditorGraphicsView.scene.addItem(rect)

# #! ==================== interface ===============================================================================
# class TimelineView(QGraphicsView):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.scene = QGraphicsScene(self)
#         self.setScene(self.scene)

#         # Örnek bir klip çiz
#         rect = QGraphicsRectItem(0, 0, 100, 50)  # x, y, width, height
#         rect.setBrush(Qt.blue)
#         self.scene.addItem(rect)


# #TODO ============ daha sonra ayrı dosyalara ayrılacak ============================================================
# class TimelineContainer:
#     def __init__(self):
#         self.tracks = []  # Video, Ses, Metin katmanları
#         self.playhead_position = 0

#     def add_track(self, track):
#         self.tracks.append(track)

#     def get_track(self, index):
#         return self.tracks[index]


# class Track:
#     def __init__(self, track_type: str):
#         self.track_type = track_type  # "video", "audio", "text"
#         self.clips = []

#     def add_clip(self, clip):
#         self.clips.append(clip)


# class Clip:
#     def __init__(self, file_path: str, start_time: int, duration: int):
#         self.file_path = file_path
#         self.start_time = start_time
#         self.duration = duration


# #! timelien wiew ----------------------------
# class TimelineView(QGraphicsView):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.scene = QGraphicsScene(self)
#         self.setScene(self.scene)

#         self.time_scale = 50  # 1 saniye = 50 piksel

#     def draw_playhead(self, position_x: int, timeline_height: int):
#         playhead = QGraphicsRectItem(position_x * self.time_scale, 0, 2, timeline_height)
#         playhead.setBrush(Qt.red)
#         self.scene.addItem(playhead)

#     def draw_clip(self, start_time: int, duration: int, y_pos: int = 0):
#         x = start_time * self.time_scale
#         width = duration * self.time_scale
#         rect = QGraphicsRectItem(x, y_pos, width, 50)
#         rect.setBrush(Qt.green)
#         self.scene.addItem(rect)


# #! özellikler ----------------------------
#         # QGraphicsScene’i yükle
#         self.timelineEditorGraphicsView.scene = QGraphicsScene(self)
#         self.timelineEditorGraphicsView.setScene(self.timelineEditorGraphicsView.scene)

#         self.time_scale = 50  # 1 saniye = 50 piksel

#         self.timeline_container = TimelineContainer()

#         # Playhead çiz
#         self.draw_playhead(0, 100)

#         # İlk video track'i ekle
#         self.timeline_container.add_track(Track(track_type="video"))

#         # Timeline görünümü
#         self.timeline_view = TimelineView(self)
#         self.timeline_height = 100
#         self.timeline_view.draw_playhead(0, self.timeline_height)

#         # İlk video track'i ekle
#         self.timeline_container.add_track(Track(track_type="video"))







