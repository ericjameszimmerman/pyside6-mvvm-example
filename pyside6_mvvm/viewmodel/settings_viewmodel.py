from PySide6.QtCore import QObject, Signal, Property


class SettingsViewModel(QObject):
    themeChanged = Signal()
    debugModeChanged = Signal()
    fontFamilyChanged = Signal()
    tabSizeChanged = Signal()

    def __init__(self, model):
        super().__init__()
        self._model = model
        self._model.themeChanged.connect(self.themeChanged)
        self._model.debugModeChanged.connect(self.debugModeChanged)
        self._model.fontFamilyChanged.connect(self.fontFamilyChanged)
        self._model.tabSizeChanged.connect(self.tabSizeChanged)

    @Property(str, notify=themeChanged)
    def theme(self):
        return self._model.theme

    @theme.setter
    def theme(self, value):
        self._model.theme = value

    def setTheme(self, value):
        self.theme = value

    @Property(bool, notify=debugModeChanged)
    def debugMode(self):
        return self._model.debugMode

    @debugMode.setter
    def debugMode(self, value):
        self._model.debugMode = value

    def setDebugMode(self, value):
        self.debugMode = value

    @Property(str, notify=fontFamilyChanged)
    def fontFamily(self):
        return self._model.fontFamily

    @fontFamily.setter
    def fontFamily(self, value):
        self._model.fontFamily = value

    def setFontFamily(self, value):
        self.fontFamily = value

    @Property(int, notify=tabSizeChanged)
    def tabSize(self):
        return self._model.tabSize

    @tabSize.setter
    def tabSize(self, value):
        self._model.tabSize = value

    def setTabSize(self, value):
        self.tabSize = value
