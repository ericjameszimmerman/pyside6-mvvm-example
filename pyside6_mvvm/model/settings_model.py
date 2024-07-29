from PySide6.QtCore import QObject, Property, Signal
from .settings_manager import SettingsManager


class SettingsModel(QObject):
    themeChanged = Signal()
    debugModeChanged = Signal()
    fontFamilyChanged = Signal()
    tabSizeChanged = Signal()

    def __init__(self):
        super().__init__()
        self.settings_manager = SettingsManager()
        self._theme = self.settings_manager.get("theme", "Light")
        self._debug_mode = True if self.settings_manager.get("debug-mode", False) else False
        self._font_family = self.settings_manager.get("font-family", "Arial")
        self._tab_size = int(self.settings_manager.get("tab-size", 4))

    def save_settings(self):
        self.settings_manager.set("theme", self._theme)
        self.settings_manager.set("debug-mode", self._debug_mode)
        self.settings_manager.set("font-family", self._font_family)
        self.settings_manager.set("tab-size", self._tab_size)
        self.settings_manager.save_settings()

    @Property(str, notify=themeChanged)
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, value):
        if self._theme != value:
            self._theme = value
            self.themeChanged.emit()

    @Property(bool, notify=debugModeChanged)
    def debugMode(self):
        return self._debug_mode

    @debugMode.setter
    def debugMode(self, value):
        if self._debug_mode != value:
            self._debug_mode = value
            self.debugModeChanged.emit()

    @Property(str, notify=fontFamilyChanged)
    def fontFamily(self):
        return self._font_family

    @fontFamily.setter
    def fontFamily(self, value):
        if self._font_family != value:
            self._font_family = value
            self.fontFamilyChanged.emit()

    @Property(int, notify=tabSizeChanged)
    def tabSize(self):
        return self._tab_size

    @tabSize.setter
    def tabSize(self, value):
        if self._tab_size != value:
            self._tab_size = value
            self.tabSizeChanged.emit()
