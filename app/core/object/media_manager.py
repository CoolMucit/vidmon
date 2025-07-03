import shutil
import os

class MediaManager:
    def __init__(self, project_path):
        self.project_path = project_path
        self.media_folder = os.path.join(project_path, "object", "media")
        os.makedirs(self.media_folder, exist_ok=True)
        self.media_files = []

    def add_media(self, file_path):
        filename = os.path.basename(file_path)
        dest_path = os.path.join(self.media_folder, filename)
        shutil.copy(file_path, dest_path)
        self.media_files.append(dest_path)
        return dest_path

    def remove_media(self, filename):
        file_path = os.path.join(self.media_folder, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            self.media_files.remove(file_path)