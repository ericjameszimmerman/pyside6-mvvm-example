from PySide6.QtCore import QObject, Property, Signal


class RichTextModel(QObject):
    contentChanged = Signal()

    def __init__(self):
        super().__init__()
        self._content = ""

    @Property(str, notify=contentChanged)
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if self._content != value:
            self._content = value
            self.contentChanged.emit()
