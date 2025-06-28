from PyQt5.QtWidgets import QListWidgetItem, QListWidget
from PyQt5 import QtGui, QtCore

class MediaPanel:
    def __init__(self, media_panel_widget: QListWidget):
        self.media_panel_widget = media_panel_widget

        self._setup_ui()

    def _setup_ui(self):
        # Görünüm: Karo
        self.media_panel_widget.setViewMode(QListWidget.IconMode)

        # Öğeler yatay olarak akacak ve sığmazsa alt satıra geçecek
        self.media_panel_widget.setFlow(QListWidget.LeftToRight)

        # Scroll bar dikey olacak (bu sayede genişleyebilir)
        self.media_panel_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.media_panel_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Icon boyutu ve kutucuk boyutu
        self.media_panel_widget.setIconSize(QtCore.QSize(64, 64))
        self.media_panel_widget.setSpacing(10)
        self.media_panel_widget.setResizeMode(QListWidget.Adjust)

        self._populate_with_sample_items()

    def _populate_with_sample_items(self):
        for i in range(12):
            item = QListWidgetItem(f"Medya {i + 1}")
            icon = QtGui.QIcon("app/assets/icons/video_icon.png")
            item.setIcon(icon)
            item.setSizeHint(QtCore.QSize(100, 100))  # Hücre boyutu
            self.media_panel_widget.addItem(item)
