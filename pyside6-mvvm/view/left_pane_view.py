from PySide6.QtWidgets import QListView


class LeftPaneView(QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(200)
        self.setSelectionMode(QListView.SingleSelection)
