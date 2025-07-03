from PyQt5.QtWidgets import QDockWidget

from PyQt5 import uic

class AudioEditorDockWidget(QDockWidget):
    def __init__(self):
        super().__init__()

        self.load_UI()

    def load_UI(self):
        uic.loadUi("app/ui/interfaces/dock_interfaces/editor_dock_interfaces/audio_editor_dock_interface.ui", self)