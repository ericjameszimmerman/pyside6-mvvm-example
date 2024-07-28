from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, QSpinBox, QPushButton, QWidget
)
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import Qt, QTimer, QDateTime


class MotorDriveView(QWidget):
    def __init__(self, viewmodel):
        super().__init__()
        self._viewmodel = viewmodel
        self.setWindowTitle("Motor Drive Simulator")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout(self)

        # Input Controls
        control_layout = QHBoxLayout()

        self.drive_enable_checkbox = QCheckBox("Drive Enable")
        self.drive_enable_checkbox.setChecked(self._viewmodel.driveEnable)
        self.drive_enable_checkbox.toggled.connect(self._viewmodel.setDriveEnable)

        self.run_forward_checkbox = QCheckBox("Run Forward")
        self.run_forward_checkbox.setChecked(self._viewmodel.runForward)
        self.run_forward_checkbox.toggled.connect(self._viewmodel.setRunForward)

        self.run_reverse_checkbox = QCheckBox("Run Reverse")
        self.run_reverse_checkbox.setChecked(self._viewmodel.runReverse)
        self.run_reverse_checkbox.toggled.connect(self._viewmodel.setRunReverse)

        self.frequency_reference_input = QSpinBox()
        self.frequency_reference_input.setRange(-100, 100)
        self.frequency_reference_input.setValue(int(self._viewmodel.frequencyReference))
        self.frequency_reference_input.valueChanged.connect(self._viewmodel.setFrequencyReference)

        control_layout.addWidget(self.drive_enable_checkbox)
        control_layout.addWidget(self.run_forward_checkbox)
        control_layout.addWidget(self.run_reverse_checkbox)
        control_layout.addWidget(QLabel("Frequency Reference:"))
        control_layout.addWidget(self.frequency_reference_input)

        layout.addLayout(control_layout)

        # Output Displays
        output_layout = QHBoxLayout()

        self.voltage_display = QLabel("Voltage: 0.0 V")
        self.current_display = QLabel("Current: 0.0 A")
        self.frequency_display = QLabel("Frequency: 0.0 Hz")
        self.rpm_display = QLabel("RPM: 0.0")

        output_layout.addWidget(self.voltage_display)
        output_layout.addWidget(self.current_display)
        output_layout.addWidget(self.frequency_display)
        output_layout.addWidget(self.rpm_display)

        layout.addLayout(output_layout)

        # Real-Time Chart
        self.series = QLineSeries()
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Output Frequency")
        self.chart.legend().hide()

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(self.chart_view)

        self.setLayout(layout)

        # Update the display values from the ViewModel
        self._viewmodel.voltageChanged.connect(self.update_voltage_display)
        self._viewmodel.currentChanged.connect(self.update_current_display)
        self._viewmodel.frequencyChanged.connect(self.update_frequency_display)
        self._viewmodel.rpmChanged.connect(self.update_rpm_display)

        # Timer to update the chart
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(100)  # Update every 100ms

        # Data storage
        self.data_points = []

    def update_voltage_display(self):
        self.voltage_display.setText(f"Voltage: {self._viewmodel.voltage:.1f} V")

    def update_current_display(self):
        self.current_display.setText(f"Current: {self._viewmodel.current:.1f} A")

    def update_frequency_display(self):
        self.frequency_display.setText(f"Frequency: {self._viewmodel.frequency:.1f} Hz")

    def update_rpm_display(self):
        self.rpm_display.setText(f"RPM: {self._viewmodel.rpm:.1f}")

    def update_chart(self):
        """
        self.series.append(self.series.count(), self._viewmodel.frequency)
        if self.series.count() > 100:  # Limit the number of points
            self.series.remove(0)

        # Adjust the axis ranges to fit the new data
        self.chart.axes(Qt.Horizontal)[0].setRange(0, self.series.count())
        self.chart.axes(Qt.Vertical)[0].setRange(min([point.y() for point in self.series.points()]),
                                                 max([point.y() for point in self.series.points()]))
        """
        # Get current timestamp
        current_time = QDateTime.currentDateTime().toMSecsSinceEpoch() / 1000.0

        # Add new data point
        self.data_points.append((current_time, self._viewmodel.frequency))

        # Remove data points older than 30 seconds
        self.data_points = [(t, f) for t, f in self.data_points if t > current_time - 30]

        # Update series
        self.series.clear()
        for t, f in self.data_points:
            self.series.append(t, f)

        # Adjust axis ranges to show only the last 30 seconds
        self.chart.axes(Qt.Horizontal)[0].setRange(current_time - 30, current_time)
        self.chart.axes(Qt.Horizontal)[0].hide()
        min_frequency = min(f for t, f in self.data_points) if self.data_points else 0
        max_frequency = max(f for t, f in self.data_points) if self.data_points else 0
        #self.chart.axes(Qt.Vertical)[0].setRange(min_frequency, max_frequency)
        self.chart.axes(Qt.Vertical)[0].setRange(-65, 65)