from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
import qtawesome as qta

class ListModel(QAbstractListModel):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self._items = items

    def rowCount(self, parent=QModelIndex()):
        return len(self._items)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < len(self._items):
            return None
        item = self._items[index.row()]
        if role == Qt.DisplayRole:
            return item.name
        if role == Qt.DecorationRole:
            return qta.icon(item.icon_name)
        return None

    def get_item(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]
        return None
