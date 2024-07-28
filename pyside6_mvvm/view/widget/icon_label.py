import qtawesome as qta
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel


class IconLabel(QWidget):

    IconSize = QSize(16, 16)
    HorizontalSpacing = 32  # Adjust the spacing as needed

    def __init__(self, qta_id, text, final_stretch=True):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(self.HorizontalSpacing)  # Set spacing between widgets
        self.setLayout(layout)

        icon = QLabel()
        icon.setPixmap(qta.icon(qta_id).pixmap(self.IconSize))

        text_label = QLabel(text)

        layout.addWidget(icon)
        layout.addWidget(text_label)

        if final_stretch:
            layout.addStretch()
