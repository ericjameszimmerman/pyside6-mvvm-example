from PySide6.QtCore import QObject, Property


class DummyViewModel(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    @Property(str)
    def data(self):
        return self._model.data
