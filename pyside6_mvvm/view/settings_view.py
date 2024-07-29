from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QCheckBox,
    QLineEdit,
    QLabel,
    QSpinBox,
    QPushButton,
)


class SettingsDialog(QDialog):
    def __init__(self, viewmodel):
        super().__init__()
        self._viewmodel = viewmodel
        self.setWindowTitle("Settings")

        self.layout = QVBoxLayout(self)

        # Theme
        self.theme_label = QLabel("Theme")
        self.theme_dropdown = QComboBox()
        self.theme_dropdown.addItems(["Light", "Dark"])
        self.theme_dropdown.setCurrentText(self._viewmodel.theme)
        self.theme_dropdown.currentTextChanged.connect(self._viewmodel.setTheme)

        # Debug Mode
        self.debug_label = QLabel("Debug Mode")
        self.debug_checkbox = QCheckBox()
        self.debug_checkbox.setChecked(self._viewmodel.debugMode)
        self.debug_checkbox.toggled.connect(self._viewmodel.setDebugMode)

        # Font Family
        self.font_label = QLabel("Font Family")
        self.font_input = QLineEdit()
        self.font_input.setText(self._viewmodel.fontFamily)
        self.font_input.textChanged.connect(self._viewmodel.setFontFamily)

        # Tab Size
        self.tab_size_label = QLabel("Tab Size")
        self.tab_size_input = QSpinBox()
        self.tab_size_input.setValue(self._viewmodel.tabSize)
        self.tab_size_input.setRange(1, 16)
        self.tab_size_input.valueChanged.connect(self._viewmodel.setTabSize)

        # Save Button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.accept)

        # Layout Setup
        self.layout.addWidget(self.theme_label)
        self.layout.addWidget(self.theme_dropdown)
        self.layout.addWidget(self.debug_label)
        self.layout.addWidget(self.debug_checkbox)
        self.layout.addWidget(self.font_label)
        self.layout.addWidget(self.font_input)
        self.layout.addWidget(self.tab_size_label)
        self.layout.addWidget(self.tab_size_input)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

        # Bind ViewModel properties to UI elements
        self._viewmodel.themeChanged.connect(lambda: self.theme_dropdown.setCurrentText(self._viewmodel.theme))
        self._viewmodel.debugModeChanged.connect(lambda: self.debug_checkbox.setChecked(self._viewmodel.debugMode))
        self._viewmodel.fontFamilyChanged.connect(lambda: self.font_input.setText(self._viewmodel.fontFamily))
        self._viewmodel.tabSizeChanged.connect(lambda: self.tab_size_input.setValue(self._viewmodel.tabSize))
