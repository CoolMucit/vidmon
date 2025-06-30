from pathlib import Path
import json

class UserProfile:
    def __init__(self, username: str, base_dir="user_data"):
        self.username = username
        self.dir = Path(base_dir) / username
        self.profile_file = self.dir / "profile.json"
        self.data = {}

    def load(self):
        if self.profile_file.exists():
            with open(self.profile_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)

    def save(self):
        self.dir.mkdir(parents=True, exist_ok=True)
        with open(self.profile_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def create_dirs(self):
        for subdir in ["layouts", "projects", "templates", "favorites"]:
            (self.dir / subdir).mkdir(parents=True, exist_ok=True)
