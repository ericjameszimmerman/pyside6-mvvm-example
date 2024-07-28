from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class DummyView(QWidget):
    def __init__(self, viewmodel):
        super().__init__()
        self._viewmodel = viewmodel

        # Set up the label and layout
        self.label = QLabel(self._viewmodel.data)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)
