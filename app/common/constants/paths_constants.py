from pathlib import Path

from app.common.utils.path_utils import find_project_root

from app.common.constants.global_constants import APP_NAME

#! === Temel yollar ===
BASE_DIR = find_project_root(APP_NAME)
# CONFIG_DIR = BASE_DIR / "config"
# LOGS_DIR = BASE_DIR / "logs"
# ASSETS_DIR = BASE_DIR / "assets"

#! === Kullanıcı dizinleri ===
# USER_HOME = Path.home()
# VIDMON_USER_DIR = USER_HOME / "VidmonProjects"

# PROFILES_DIR = VIDMON_USER_DIR / "Profiles"
# PROJECTS_DIR = VIDMON_USER_DIR / "Projects"
# EXPORTS_DIR = VIDMON_USER_DIR / "Exports"
# IMPORTS_DIR = VIDMON_USER_DIR / "Imports"
# CACHE_DIR = VIDMON_USER_DIR / ".cache"
# TEMP_DIR = VIDMON_USER_DIR / "Temp"
# BACKUPS_DIR = VIDMON_USER_DIR / "Backups"

#! === Diğer yollar ===
# LOCALES_DIR = ASSETS_DIR / "locales"
# ICONS_DIR = ASSETS_DIR / "icons"
# THEMES_DIR = ASSETS_DIR / "themes"
# PLACEHOLDER_MEDIA = ASSETS_DIR / "placeholders" / "default_video.mp4"

#! === Log dosyaları ===
# APP_LOG_FILE = LOGS_DIR / "app.log"
# ERROR_LOG_FILE = LOGS_DIR / "error.log"
