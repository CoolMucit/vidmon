from pathlib import Path

#! === Proje kök dizinini otomatik bul ===
def find_project_root(project_folder_name) -> Path:
    path = Path(__file__).resolve()
    while path.name != project_folder_name:
        if path.parent == path:
            raise RuntimeError(f"Proje kökü ({project_folder_name}) bulunamadı.")
        path = path.parent
    return path

# def ensure_dir_exists(path: Path):
#     """Verilen dizin yoksa oluşturur."""
#     if not path.exists():
#         path.mkdir(parents=True, exist_ok=True)

# def is_writable(path: Path) -> bool:
#     """Yol yazılabilir mi kontrol eder (klasör veya dosya olabilir)."""
#     try:
#         if path.is_dir():
#             test_file = path / ".test_write"
#         else:
#             test_file = path

#         with open(test_file, 'w') as f:
#             f.write('')
#         if path.is_dir():
#             test_file.unlink()
#         return True
#     except Exception:
#         return False

# def create_default_dirs(*dirs: Path):
#     """Birden fazla klasör verilip hepsi oluşturulur."""
#     for d in dirs:
#         ensure_dir_exists(d)
