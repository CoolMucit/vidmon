import sys
from PyQt5.QtWidgets import QApplication
from app.ui.launch_window import LaunchWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launch_window = LaunchWindow()
    launch_window.show()
    sys.exit(app.exec_())
