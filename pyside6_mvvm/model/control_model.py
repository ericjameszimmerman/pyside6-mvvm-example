# model.py
from PySide6.QtCore import QObject, Signal


class ControlModel(QObject):
    dataChanged = Signal()

    def __init__(self):
        super().__init__()
        self._data = {
            "toggle": False,
            "checkbox": False,
            "momentary_button": False,
            "latching_button": False,
            "text": "",
        }

    def get_data(self, key):
        return self._data.get(key)

    def set_data(self, key, value):
        if key in self._data:
            self._data[key] = value
            self.dataChanged.emit()
