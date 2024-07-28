from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt


class ThemeBase:
    def __init__(self, app):
        self.app = app
        self.palette = app.palette()
        self.default_text_color = 'black'

    def apply(self):
        self.app.setPalette(self.palette)

    def set_common_colors(self):
        self.palette.setColor(QPalette.ToolTipBase, Qt.white)
        self.palette.setColor(QPalette.ToolTipText, Qt.white)
        self.palette.setColor(QPalette.BrightText, Qt.red)
        self.palette.setColor(QPalette.Link, QColor(42, 130, 218))
        self.palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.palette.setColor(
            QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80)
        )
        self.palette.setColor(QPalette.HighlightedText, Qt.white)
        self.palette.setColor(
            QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127)
        )