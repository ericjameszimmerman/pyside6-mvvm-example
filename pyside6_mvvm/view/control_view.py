# view.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QCheckBox, QPushButton, QLineEdit, QApplication
import pyside6_mvvm.view.widget as widget


class ControlView(QWidget):
    def __init__(self, viewmodel):
        super().__init__()
        self.viewmodel = viewmodel
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        wrap_widget = QWidget()
        wrap_layout = widget.WrapLayout()

        toggle_switch = widget.ToggleSwitch()
        toggle_switch.setFixedWidth(150)
        # toggle_switch.mouseReleaseEvent = lambda event: self.viewmodel.set_data('toggle', toggle_switch.isChecked())
        toggle_switch.mouseReleaseEvent = lambda event: self.toggle_switch_clicked(event, toggle_switch)

        checkbox = QCheckBox("Checkbox")
        checkbox.setFixedWidth(150)
        checkbox.stateChanged.connect(lambda state: self.viewmodel.set_data("checkbox", state == Qt.Checked))

        momentary_button = QPushButton("Momentary Button")
        momentary_button.setFixedWidth(150)
        momentary_button.pressed.connect(lambda: self.viewmodel.set_data("momentary_button", True))
        momentary_button.released.connect(lambda: self.viewmodel.set_data("momentary_button", False))

        latching_button = QPushButton("Latching Button")
        latching_button.setFixedWidth(150)
        latching_button.setCheckable(True)
        latching_button.toggled.connect(lambda state: self.viewmodel.set_data("latching_button", state))

        text_box = QLineEdit()
        text_box.setFixedWidth(150)
        text_box.textChanged.connect(lambda text: self.viewmodel.set_data("text", text))

        wrap_layout.addWidget(toggle_switch)
        wrap_layout.addWidget(checkbox)
        wrap_layout.addWidget(momentary_button)
        wrap_layout.addWidget(latching_button)
        wrap_layout.addWidget(text_box)

        wrap_widget.setLayout(wrap_layout)
        scroll_area.setWidget(wrap_widget)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def toggle_switch_clicked(self, event, toggle_switch):
        if event.button() == Qt.LeftButton:
            toggle_switch.setChecked(not toggle_switch.isChecked())
            self.viewmodel.set_data("toggle", toggle_switch.isChecked())
