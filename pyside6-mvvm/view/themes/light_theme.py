from .theme_base import ThemeBase
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

class LightTheme(ThemeBase):
    def __init__(self, app):
        super().__init__(app)
        self.set_theme_colors()
        self.set_common_colors()

    def set_theme_colors(self):
        self.palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.palette.setColor(QPalette.WindowText, Qt.black)
        self.palette.setColor(
            QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127)
        )
        self.palette.setColor(QPalette.Base, QColor(240, 240, 240))
        self.palette.setColor(QPalette.AlternateBase, QColor(225, 225, 225))
        self.palette.setColor(QPalette.ToolTipBase, Qt.black)
        self.palette.setColor(QPalette.Text, Qt.black)
        self.palette.setColor(
            QPalette.Disabled, QPalette.Text, QColor(127, 127, 127)
        )
        self.palette.setColor(QPalette.Dark, QColor(200, 200, 200))
        self.palette.setColor(QPalette.Shadow, QColor(150, 150, 150))
        self.palette.setColor(QPalette.Button, QColor(240, 240, 240))
        self.palette.setColor(QPalette.ButtonText, Qt.black)
        self.palette.setColor(
            QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127)
        )
