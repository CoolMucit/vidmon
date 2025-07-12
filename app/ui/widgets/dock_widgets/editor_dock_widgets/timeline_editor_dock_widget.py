from PyQt5.QtWidgets import QDockWidget, QGraphicsView, QPushButton, QSlider
from PyQt5 import uic

from app.core.editor.timeline.timeline_scene import TimelineScene
from app.core.editor.timeline.timeline_scale import TimelineScale


class TimelineEditorDockWidget(QDockWidget):
    def __init__(self):
        super().__init__()

        # UI yükle ve elemanları bul
        self.load_UI()
        self.find_UI_elements()

        #! EDITOR SAHNESİNİ OLUŞTUR
        self.timeline_scene = TimelineScene()
        self.timelineEditorGraphicsView.setScene(self.timeline_scene)

        # Scale kontrolü
        self.timeline_scale = TimelineScale(self.timelineScaleControlSlider)
        self.timeline_scale.ruler_ref = self.timeline_scene.timeline_ruler  # Ruler referansı ver
        #! Scale slider değiştiğinde çağrılacak metodu bağla
        self.timelineScaleControlSlider.valueChanged.connect(self.on_scale_slider_changed)


    def load_UI(self):
        uic.loadUi("app/ui/interfaces/dock_interfaces/editor_dock_interfaces/timeline_editor_dock_interface.ui", self)

    def find_UI_elements(self):
        self.timelineEditorGraphicsView: QGraphicsView = self.findChild(QGraphicsView, "timelineEditorGraphicsView")
        self.timelineScaleControlSlider: QSlider = self.findChild(QSlider, "timelineScaleControlSlider")
        self.timelineCreateTrackButton: QPushButton = self.findChild(QPushButton, "timelineCreateTrackButton")
        self.timelineRemoveTrackButton: QPushButton = self.findChild(QPushButton, "timelineRemoveTrackButton")

    def on_scale_slider_changed(self, value: int):
        """
        Slider değeri değiştiğinde zaman cetvelinin ölçeğini günceller.
        """
        # TimelineScale üzerinden scale faktörünü al
        scale_factor = self.timeline_scale.get_current_pixel_per_second()

        print(f"[Slider] Scale factor güncellendi: {scale_factor:.2f} px/s")

        # TimelineRuler'ın ölçeğini güncelle
        self.timeline_scene.timeline_ruler.set_scale_factor(scale_factor)

        # Sahne boyutunu güncelle (gerekiyorsa)
        scene_width = self.timeline_scene.timeline_ruler.duration * scale_factor + self.timeline_scene.timeline_ruler.trackHeaderWidth
        self.timeline_scene.setSceneRect(0, 0, scene_width, self.timeline_scene.sceneRect().height())

        # Yeniden çiz
        self.timeline_scene.timeline_ruler.update()

