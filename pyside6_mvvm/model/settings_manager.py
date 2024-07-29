import os
import toml
from pathlib import Path


class SettingsManager:
    def __init__(self, filename="settings.toml"):
        self.filename = filename
        self.settings_path = self.get_settings_path()
        self.settings = self.load_settings()

    def get_settings_path(self):
        # Determine the user-specific directory based on the OS
        if os.name == "nt":  # Windows
            base_dir = Path(os.getenv("APPDATA", ""))
        else:  # Linux and other Unix-like systems
            base_dir = Path(os.getenv("XDG_CONFIG_HOME", Path.home() / ".config"))

        settings_dir = base_dir / "pyside6-mvvm"
        settings_dir.mkdir(parents=True, exist_ok=True)
        return settings_dir / self.filename

    def load_settings(self):
        if self.settings_path.is_file():
            with open(self.settings_path, "r") as file:
                return toml.load(file)
        return {}

    def save_settings(self):
        with open(self.settings_path, "w") as file:
            toml.dump(self.settings, file)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save_settings()

    def delete(self, key):
        if key in self.settings:
            del self.settings[key]
            self.save_settings()
