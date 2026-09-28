from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="allow", env_file=".env", env_file_encoding="utf-8")

    # App details - main.py ku thevai
    app_name: str = "ComicCraft AI"
    app_version: str = "1.0.0"
    
    # All folders
    static_dir: Path = BASE_DIR / "app" / "static"
    panel_dir: Path = BASE_DIR / "panels"
    panels_dir: Path = BASE_DIR / "panels"
    upload_dir: Path = BASE_DIR / "uploads"
    uploads_dir: Path = BASE_DIR / "uploads"
    export_dir: Path = BASE_DIR / "exports"
    exports_dir: Path = BASE_DIR / "exports"
    templates_dir: Path = BASE_DIR / "app" / "templates"

settings = Settings()

# Auto create folders
for p in [settings.static_dir, settings.panel_dir, settings.upload_dir, settings.export_dir]:
    p.mkdir(parents=True, exist_ok=True)