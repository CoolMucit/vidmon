from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QDockWidget
from PyQt5.QtCore import Qt
from PyQt5 import uic
import os

from app.ui.widgets.dock_widgets.dock_widget_registry import DockWidgetRegistry

from app.common.constants.global_constants import APP_NAME
from app.core.controllers.dock_manager import DockManager
from app.profiles.user_profile import UserProfile
from app.common.signals.signals import signals


class MainWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()

        self.username = username
        self.dock_manager = DockManager(self, self.username)

        self.docks = DockWidgetRegistry()
        # Dockları otomatik ekle ve sekmeli yap
        self.add_docks_from_registry(self.docks)



        # Dock'ları ekle
        # self._add_existing_docks()

        # UI yükle
        self.load_UI()

        # Menü elemanlarını bul ve bağla
        self.find_UI_elements()

        # Stil, kullanıcı profili ve pencere ayarlarını yükle
        self.load_styles()
        self.load_user_profile(self.username)
        self.load_options(self.username)

        # Varsayılan layoutu yükle (Varsa)
        self.dock_manager.load_dock_layout("Default")

    def load_UI(self):
        uic.loadUi("app/ui/interfaces/main_window_interface.ui", self)

    def find_UI_elements(self):
        # Menüdeki QActionları bul
        self.actionSaveDocks: QAction = self.findChild(QAction, "actionSaveDocks")
        self.actionMyDocks: QAction = self.findChild(QAction, "actionMyDocks")

        # actionMyDocks'u QMenu'ya dönüştür
        self.menuMyDocks = QMenu("Kayıtlı Paneller", self)
        self.actionMyDocks.setMenu(self.menuMyDocks)

        # Panelleri Kaydet butonunu DockManager’a bağla
        self.actionSaveDocks.triggered.connect(self.dock_manager.save_dock_layout)

        # Kayıtlı layoutları doldurmak için aboutToShow sinyaline bağlan
        self.menuMyDocks.aboutToShow.connect(self.populate_my_docks_menu)

    def populate_my_docks_menu(self):
        # Menüdeki eski elemanları temizle
        self.menuMyDocks.clear()

        # Kullanıcının kayıtlı layoutlarını al
        layouts = self.dock_manager.list_layouts()

        if not layouts:
            # Eğer hiç layout yoksa pasif bir item ekle
            no_layout_action = self.menuMyDocks.addAction("(Kayıtlı panel yok)")
            no_layout_action.setEnabled(False)
        else:
            # Her kayıtlı layout için bir QAction oluştur
            for layout_name in layouts:
                action = self.menuMyDocks.addAction(layout_name)

                # Lambda yerine ayrı bir callback metodu kullan (closure hatası yok)
                action.triggered.connect(
                    self._make_load_layout_callback(layout_name)
                )

    def _make_load_layout_callback(self, layout_name):
        return lambda checked: self.dock_manager.load_dock_layout(layout_name)

    def load_styles(self):
        style_path = os.path.join("app", "assets", "styles", "main_window.qss")
        with open(style_path, "r") as file:
            style = file.read()
            self.setStyleSheet(style)

    def load_user_profile(self, username):
        self.user_profile = UserProfile(username)
        self.user_profile.load()

    def load_options(self, username):
        self.setWindowTitle(APP_NAME + f" ({username})")
        # self.showMaximized()

    def closeEvent(self, event):
        signals.main_window_closed.emit()
        super().closeEvent(event)

    def _add_existing_docks(self):

        self.docks.object["media"].setParent(self)
        self.docks.player["preview"].setParent(self)
        self.docks.property["global"].setParent(self)
        self.docks.editor["timeline"].setParent(self)

        # Dock’ların yapışabileceği alanları belirt
        self.docks.object["media"].setAllowedAreas(Qt.AllDockWidgetAreas)
        self.docks.player["preview"].setAllowedAreas(Qt.AllDockWidgetAreas)
        self.docks.property["global"].setAllowedAreas(Qt.AllDockWidgetAreas)
        self.docks.editor["timeline"].setAllowedAreas(Qt.AllDockWidgetAreas)

        # Dock’ları MainWindow’a yerleştir
        self.addDockWidget(Qt.TopDockWidgetArea, self.docks.object["media"])
        self.addDockWidget(Qt.TopDockWidgetArea, self.docks.player["preview"])
        self.addDockWidget(Qt.TopDockWidgetArea, self.docks.property["global"])
        self.addDockWidget(Qt.BottomDockWidgetArea, self.docks.editor["timeline"])

        # Dock referanslarını sakla
        self.media_object_dock = self.docks.object["media"]
        self.preview_player_dock = self.docks.player["preview"]
        self.global_property_dock = self.docks.property["global"]
        self.timeline_editor_dock = self.docks.editor["timeline"]

    def add_docks_from_registry(self, dock_registry):
        for group, docks in dock_registry.__dict__.items():
            if group == "dock_areas":  # ❌ dock_areas'ı atla
                continue

            if isinstance(docks, dict):
                dock_area = dock_registry.dock_areas.get(group, Qt.LeftDockWidgetArea)
                dock_list = list(docks.values())

                for dock in dock_list:
                    if not hasattr(dock, "setParent"):  # QDockWidget kontrolü
                        print(f"❌ HATALI DOCK: {group} içindeki {dock} ({type(dock)})")
                        continue

                    dock.setParent(self)
                    dock.setAllowedAreas(Qt.AllDockWidgetAreas)
                    self.addDockWidget(dock_area, dock)

                self._tabify_group(dock_list)




    def _tabify_group(self, dock_list):
        """
        Verilen dock listesindeki dock'ları sekmeli gruplar.
        """
        if not dock_list:
            return

        base_dock = dock_list[0]
        for dock in dock_list[1:]:
            self.tabifyDockWidget(base_dock, dock)










