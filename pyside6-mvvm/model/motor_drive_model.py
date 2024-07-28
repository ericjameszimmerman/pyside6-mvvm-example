import time
import threading
from PySide6.QtCore import QObject, Property, Signal
from .pid_controller import PIDController


class MotorDriveModel(QObject):
    voltageChanged = Signal()
    currentChanged = Signal()
    frequencyChanged = Signal()
    rpmChanged = Signal()

    def __init__(self):
        super().__init__()
        self._drive_enable = False
        self._run_forward = False
        self._run_reverse = False
        self._frequency_reference = 60.0
        self._voltage = 0.0
        self._current = 0.0
        self._frequency = 0.0
        self._rpm = 0.0
        self._running = True
        self._pid = PIDController(kp=0.5, ki=0, kd=0)
        self._target_frequency = 0.0

        # Start the motor simulation thread
        self._thread = threading.Thread(target=self._simulate_motor)
        self._thread.start()

    @Property(bool)
    def driveEnable(self):
        return self._drive_enable

    @driveEnable.setter
    def driveEnable(self, value):
        self._drive_enable = value
        self._update_state()

    @Property(bool)
    def runForward(self):
        return self._run_forward

    @runForward.setter
    def runForward(self, value):
        self._run_forward = value
        self._update_state()

    @Property(bool)
    def runReverse(self):
        return self._run_reverse

    @runReverse.setter
    def runReverse(self, value):
        self._run_reverse = value
        self._update_state()

    @Property(float)
    def frequencyReference(self):
        return self._frequency_reference

    @frequencyReference.setter
    def frequencyReference(self, value):
        self._frequency_reference = value
        self._update_state()

    @Property(float, notify=voltageChanged)
    def voltage(self):
        return self._voltage

    @Property(float, notify=currentChanged)
    def current(self):
        return self._current

    @Property(float, notify=frequencyChanged)
    def frequency(self):
        return self._frequency

    @Property(float, notify=rpmChanged)
    def rpm(self):
        return self._rpm

    def _update_state(self):
        if self._drive_enable:
            if self._run_forward and not self._run_reverse:
                self._target_frequency = self._frequency_reference
            elif self._run_reverse and not self._run_forward:
                self._target_frequency = -self._frequency_reference
            else:
                self._target_frequency = 0
        else:
            self._target_frequency = 0

    def _simulate_motor(self):
        while self._running:
            time.sleep(0.1)
            control_signal = self._pid.compute(self._target_frequency, self._frequency)
            self._frequency += control_signal * 0.1  # Apply control signal with a gain factor
            self._rpm = self._frequency * 60
            self._voltage = abs(self._frequency) * 2
            self._current = abs(self._frequency) * 1.5
            self.frequencyChanged.emit()
            self.rpmChanged.emit()
            self.voltageChanged.emit()
            self.currentChanged.emit()

    def stop(self):
        self._running = False
        self._thread.join()
