from PyQt5.QtWidgets import QGraphicsScene

from app.core.editor.timeline.timeline_ruler import TimelineRuler
from app.core.editor.timeline.timeline_track import TimelineTrack


class TimelineScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSceneRect(0, 0, 2000, 500)
        self.trackList: list[TimelineTrack] = [] 
        self.create_track(0, 0, "Video Track 1", 0)

        scaleFactor = 50  # 1 saniye = 50px
        startTime = 0     # Zamanın başlangıcı
        duration = 60     # 60 saniyelik cetvel
        headerWidth = 150 # Track header genişliği
        fps = 25          # Frame rate

        # Cetveli oluştur ve sahneye ekle
        self.timeline_ruler = TimelineRuler(scaleFactor, startTime, duration, headerWidth, fps)
        self.addItem(self.timeline_ruler)

    def create_track(self, x: int, y: int, name: str, index: int, width: int = 800, height: int = 100):

        if y is None:
            scene_height = self.sceneRect().height()
            y = (scene_height / 2) - (height / 2)

        track = TimelineTrack(x, y, width, height, track_name=name, track_index=index)
        self.trackList.append(track)
        self.addItem(track)



