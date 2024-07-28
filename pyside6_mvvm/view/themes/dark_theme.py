from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from .theme_base import ThemeBase
import sys


class DarkTheme(ThemeBase):
    def __init__(self, app):
        super().__init__(app)
        self.set_theme_colors()
        self.set_common_colors()

    def set_theme_colors(self):
        self.default_text_color = "white"
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.WindowText, Qt.white)
        self.palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
        self.palette.setColor(QPalette.Base, QColor(42, 42, 42))
        self.palette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
        self.palette.setColor(QPalette.Dark, QColor(35, 35, 35))
        self.palette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
