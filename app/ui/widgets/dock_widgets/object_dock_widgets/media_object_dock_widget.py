from PyQt5.QtWidgets import QDockWidget, QListWidget, QPushButton, QFileDialog, QVBoxLayout, QWidget

from PyQt5 import uic

class MediaObjectDockWidget(QDockWidget):
    def __init__(self):
        super().__init__()

        self.load_UI()
        self.find_UI_elements()

        self.setup_signals()

        

    def load_UI(self):
        uic.loadUi("app/ui/interfaces/dock_interfaces/object_dock_interfaces/media_object_dock_interface.ui", self)

    def find_UI_elements(self):
        self.mediaObjectItemList: QListWidget = self.findChild(QListWidget, "mediaObjectItemList")
        self.mediaObjectImportButton: QPushButton = self.findChild(QPushButton, "mediaObjectImportButton")
        self.mediaObjectDeleteButton: QPushButton = self.findChild(QPushButton, "mediaObjectDeleteButton")

    def setup_signals(self):
        self.mediaObjectImportButton.clicked.connect(self.add_media)
        self.mediaObjectDeleteButton.clicked.connect(self.remove_media)

    def add_media(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Video Dosyası Seç", "", "Video Files (*.mp4 *.avi)")
        if file_path:
            self.mediaObjectItemList.addItem(file_path)

    def remove_media(self):
        selected_item = self.mediaObjectItemList.currentItem()
        if selected_item:
            self.mediaObjectItemList.takeItem(self.mediaObjectItemList.row(selected_item))