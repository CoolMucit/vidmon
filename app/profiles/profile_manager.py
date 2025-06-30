from pathlib import Path
from .user_profile import UserProfile
import shutil

class ProfileManager:
    def __init__(self, base_dir="user_data"):
        self.base_dir = Path(base_dir)

    def list_profiles(self):
        return [p.name for p in self.base_dir.iterdir() if p.is_dir()]

    def create_profile(self, username):
        profile = UserProfile(username, base_dir=self.base_dir)
        profile.data = {
            "username": username,
            "created_at": "2025-06-29T00:00:00"
        }
        profile.create_dirs()
        profile.save()
        return profile

    def delete_profile(self, username):
        shutil.rmtree(self.base_dir / username, ignore_errors=True)

    def profile_exists(self, username):
        return (self.base_dir / username).exists()
