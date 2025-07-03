from PyQt5.QtWidgets import QDockWidget, QPushButton, QSlider, QVBoxLayout, QHBoxLayout, QWidget, QGraphicsView
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

from PyQt5 import uic

class PreviewPlayerDockWidget(QDockWidget):
    def __init__(self):
        super().__init__()

        self.load_UI()
        self.find_UI_elements()

        self.video_widget = QVideoWidget()
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)

    def load_UI(self):
        uic.loadUi("app/ui/interfaces/dock_interfaces/player_dock_interfaces/preview_player_dock_interface.ui", self)

    def find_UI_elements(self):
        self.graphicsViewPreviewPlayer: QGraphicsView = self.findChild(QGraphicsView, "graphicsViewPreviewPlayer")
        self.fullScreenPreviewPlayerButton: QPushButton = self.findChild(QPushButton, "fullScreenPreviewPlayerButton")
        self.stopTimelinePreviewPlayerButton: QPushButton = self.findChild(QPushButton, "stopTimelinePreviewPlayerButton")
        self.previousFramePreviewPlayerButton: QPushButton = self.findChild(QPushButton, "previousFramePreviewPlayerButton")
        self.previousItemPreviewPlayerButton: QPushButton = self.findChild(QPushButton, "previousItemPreviewPlayerButton")
        self.nextFramePreviewPlayerButton: QPushButton = self.findChild(QPushButton, "nextFramePreviewPlayerButton")
        self.nextItemPreviewPlayerButton: QPushButton = self.findChild(QPushButton, "nextItemPreviewPlayerButton")

        










