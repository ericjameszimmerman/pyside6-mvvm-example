from PySide6.QtWidgets import QListView


class LeftPaneView(QListView):
    def __init__(self, viewmodel, parent=None):
        super().__init__(parent)
        self._viewmodel = viewmodel
        self.setFixedWidth(200)
        self.setSelectionMode(QListView.SingleSelection)
        self.setModel(self._viewmodel.list_model)

        # Select the first item
        if self.model().rowCount() > 0:
            self.setCurrentIndex(self.model().index(0, 0))

    def get_selected_model(self):
        current_index = self.currentIndex()
        if current_index.isValid():
            return self._viewmodel.get_item_model(current_index.row())
        return None
