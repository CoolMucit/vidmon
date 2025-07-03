import os
from PyQt5.QtWidgets import QInputDialog

class DockManager:
    def __init__(self, main_window, username):
        self.main_window = main_window
        self.username = username
        self.layouts_dir = os.path.join("user_data", self.username, "layouts")
        os.makedirs(self.layouts_dir, exist_ok=True)

    def save_dock_layout(self):
        # İsim sor
        layout_name, ok = QInputDialog.getText(
            self.main_window, "Paneli Kaydet", "Panel düzenine bir isim verin:"
        )

        # Kullanıcı Tamam'a bastıysa ve isim boş değilse kaydet
        if ok and layout_name:
            layout_file = os.path.join(self.layouts_dir, f"{layout_name}.bin")
            geometry = self.main_window.saveGeometry()
            state = self.main_window.saveState()
            with open(layout_file, "wb") as f:
                f.write(geometry + b"||" + state)
            print(f"[DockManager] Layout kaydedildi: {layout_file}")

    def load_dock_layout(self, layout_name):
        layout_file = os.path.join(self.layouts_dir, f"{layout_name}.bin")
        if os.path.exists(layout_file):
            with open(layout_file, "rb") as f:
                data = f.read()
                geometry, state = data.split(b"||")
                self.main_window.restoreGeometry(geometry)
                self.main_window.restoreState(state)
            print(f"[DockManager] Layout yüklendi: {layout_file}")
        else:
            print(f"[DockManager] Layout bulunamadı: {layout_file}")

    def list_layouts(self):
        # Tüm layout dosyalarını listele
        layouts = []
        if os.path.exists(self.layouts_dir):
            for file in os.listdir(self.layouts_dir):
                if file.endswith(".bin"):
                    layouts.append(os.path.splitext(file)[0])  # ".bin" uzantısını çıkar
        return layouts
