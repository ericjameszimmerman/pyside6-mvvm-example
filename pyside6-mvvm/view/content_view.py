from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ContentView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def display_content(self, content):
        # Clear previous content
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Add new content
        label = QLabel(content)
        self.layout.addWidget(label)