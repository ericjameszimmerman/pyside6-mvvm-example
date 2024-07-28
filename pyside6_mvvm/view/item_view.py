import qtawesome as qta
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel


class ItemView(QWidget):

    IconSize = QSize(16, 16)
    HorizontalSpacing = 32  # Adjust the spacing as needed

    def __init__(self, viewmodel):
        super().__init__()
        self._viewmodel = viewmodel
        self._init_ui()

    def _init_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(self.HorizontalSpacing)  # Set spacing between widgets
        self.setLayout(layout)

        icon = QLabel()
        icon.setPixmap(qta.icon(self._viewmodel.icon_path).pixmap(self.IconSize))

        text_label = QLabel(self._viewmodel.name)

        layout.addWidget(icon)
        layout.addWidget(text_label)

        layout.addStretch()
