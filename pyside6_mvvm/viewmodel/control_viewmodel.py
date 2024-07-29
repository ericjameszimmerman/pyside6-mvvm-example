# viewmodel.py
from PySide6.QtCore import QObject, Signal


class ControlViewModel(QObject):
    dataChanged = Signal()

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.model.dataChanged.connect(self.dataChanged)

    def get_data(self, key):
        return self.model.get_data(key)

    def set_data(self, key, value):
        self.model.set_data(key, value)
