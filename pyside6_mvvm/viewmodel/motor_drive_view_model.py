from PySide6.QtCore import QObject, Signal, Property


class MotorDriveViewModel(QObject):
    driveEnableChanged = Signal()
    runForwardChanged = Signal()
    runReverseChanged = Signal()
    frequencyReferenceChanged = Signal()
    voltageChanged = Signal()
    currentChanged = Signal()
    frequencyChanged = Signal()
    rpmChanged = Signal()

    def __init__(self, model_arg):
        super().__init__()
        self._model = model_arg
        self._model.voltageChanged.connect(self.voltageChanged)
        self._model.currentChanged.connect(self.currentChanged)
        self._model.frequencyChanged.connect(self.frequencyChanged)
        self._model.rpmChanged.connect(self.rpmChanged)

    @Property(bool, notify=driveEnableChanged)
    def driveEnable(self):
        return self._model.driveEnable

    @driveEnable.setter
    def driveEnable(self, value):
        self._model.driveEnable = value
        self.driveEnableChanged.emit()

    def setDriveEnable(self, value):
        self.driveEnable = value

    @Property(bool, notify=runForwardChanged)
    def runForward(self):
        return self._model.runForward

    @runForward.setter
    def runForward(self, value):
        self._model.runForward = value
        self.runForwardChanged.emit()

    def setRunForward(self, value):
        self.runForward = value

    @Property(bool, notify=runReverseChanged)
    def runReverse(self):
        return self._model.runReverse

    @runReverse.setter
    def runReverse(self, value):
        self._model.runReverse = value
        self.runReverseChanged.emit()

    def setRunReverse(self, value):
        self.runReverse = value

    @Property(float, notify=frequencyReferenceChanged)
    def frequencyReference(self):
        return self._model.frequencyReference

    @frequencyReference.setter
    def frequencyReference(self, value):
        self._model.frequencyReference = value
        self.frequencyReferenceChanged.emit()

    def setFrequencyReference(self, value):
        self.frequencyReference = value

    @Property(float, notify=voltageChanged)
    def voltage(self):
        return self._model.voltage

    @Property(float, notify=currentChanged)
    def current(self):
        return self._model.current

    @Property(float, notify=frequencyChanged)
    def frequency(self):
        return self._model.frequency

    @Property(float, notify=rpmChanged)
    def rpm(self):
        return self._model.rpm
