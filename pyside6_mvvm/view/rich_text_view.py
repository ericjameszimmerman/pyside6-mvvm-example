import qtawesome as qta
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QToolBar
from PySide6.QtGui import QIcon, QAction


class RichTextView(QWidget):
    def __init__(self, viewmodel):
        super().__init__()
        self._viewmodel = viewmodel
        self._init_ui()
        self._viewmodel.initialize_content()

    def _init_ui(self):
        layout = QVBoxLayout(self)

        # Text Edit
        self.text_edit = QTextEdit()
        self.text_edit.setFontFamily("Arial")
        self._viewmodel.bind_text_edit(self.text_edit)
        layout.addWidget(self.text_edit)

        # Toolbar
        toolbar = QToolBar()

        bold_action = QAction(qta.icon("fa.bold"), "", self)
        bold_action.triggered.connect(lambda: self._viewmodel.formatText("bold"))
        toolbar.addAction(bold_action)

        italic_action = QAction(qta.icon("fa.italic"), "", self)
        italic_action.triggered.connect(lambda: self._viewmodel.formatText("italic"))
        toolbar.addAction(italic_action)

        underline_action = QAction(qta.icon("fa.underline"), "", self)
        underline_action.triggered.connect(lambda: self._viewmodel.formatText("underline"))
        toolbar.addAction(underline_action)

        increase_font_action = QAction(qta.icon("fa.plus"), "", self)
        increase_font_action.triggered.connect(self._viewmodel.increaseFontSize)
        toolbar.addAction(increase_font_action)

        decrease_font_action = QAction(qta.icon("fa.minus"), "", self)
        decrease_font_action.triggered.connect(self._viewmodel.decreaseFontSize)
        toolbar.addAction(decrease_font_action)

        layout.setMenuBar(toolbar)
        self.setLayout(layout)
