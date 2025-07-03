from PyQt5.QtWidgets import QDockWidget

from PyQt5 import uic

class AssetPlayerDockWidget(QDockWidget):
    def __init__(self):
        super().__init__()

        self.load_UI()

    def load_UI(self):
        uic.loadUi("app/ui/interfaces/dock_interfaces/player_dock_interfaces/asset_player_dock_interface.ui", self)
