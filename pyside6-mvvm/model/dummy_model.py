from PySide6.QtCore import QObject

class DummyModel(QObject):
    def __init__(self):
        super().__init__()
        self._data = "Dummy View"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
