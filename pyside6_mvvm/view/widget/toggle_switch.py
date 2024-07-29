# toggleswitch.py
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QSize, Qt, QRect
from PySide6.QtGui import QColor, QPainter, QBrush, QMouseEvent


class ToggleSwitch(QWidget):
    def __init__(self, parent=None):
        super(ToggleSwitch, self).__init__(parent)
        self.setFixedSize(60, 30)
        self._checked = False
        self._disabled = False
        self._bg_color = QColor("#777")
        self._circle_color = QColor("#DDD")
        self._checked_color = QColor("#00B16A")
        self._circle_disabled_color = QColor("#AAA")

    def sizeHint(self):
        return QSize(60, 30)

    def isChecked(self):
        return self._checked

    def setChecked(self, checked):
        self._checked = checked
        self.update()

    def isDisabled(self):
        return self._disabled

    def setDisabled(self, disabled):
        self._disabled = disabled
        self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if not self._disabled and event.button() == Qt.LeftButton:
            self._checked = not self._checked
            self.update()
            self.clicked.emit(self._checked)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # Draw background
        rect = self.rect()
        bg_brush = QBrush(self._bg_color)
        if self._checked:
            bg_brush.setColor(self._checked_color)
        painter.setBrush(bg_brush)
        painter.drawRoundedRect(rect, rect.height() / 2, rect.height() / 2)

        # Draw circle
        circle_rect = QRect(3, 3, rect.height() - 6, rect.height() - 6)
        circle_brush = QBrush(self._circle_color)
        if self._disabled:
            circle_brush.setColor(self._circle_disabled_color)
        elif self._checked:
            circle_rect.moveLeft(rect.width() - circle_rect.width() - 3)
        painter.setBrush(circle_brush)
        painter.drawEllipse(circle_rect)
