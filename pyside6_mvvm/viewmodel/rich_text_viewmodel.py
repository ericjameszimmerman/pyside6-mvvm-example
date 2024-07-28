from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QTextCursor


class RichTextViewModel(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._model.contentChanged.connect(self.onContentChanged)
        self._is_updating = False

    @Slot(str)
    def setContent(self, content):
        self._model.content = content

    @Slot(str)
    def formatText(self, format_type):
        cursor = self.textEdit.textCursor()
        if format_type == "bold":
            cursor.mergeCharFormat(self._get_char_format(bold=True))
        elif format_type == "italic":
            cursor.mergeCharFormat(self._get_char_format(italic=True))
        elif format_type == "underline":
            cursor.mergeCharFormat(self._get_char_format(underline=True))
        self.textEdit.setTextCursor(cursor)

    def onContentChanged(self):
        if not self._is_updating:
            self._is_updating = True
            cursor = self.textEdit.textCursor()
            self.textEdit.setHtml(self._model.content)
            self.textEdit.setTextCursor(cursor)
            self._is_updating = False

    def _get_char_format(self, bold=False, italic=False, underline=False):
        char_format = self.textEdit.currentCharFormat()
        if bold:
            char_format.setFontWeight(75 if char_format.fontWeight() != 75 else 50)
        if italic:
            char_format.setFontItalic(not char_format.fontItalic())
        if underline:
            char_format.setFontUnderline(not char_format.fontUnderline())
        return char_format

    @Slot()
    def increaseFontSize(self):
        cursor = self.textEdit.textCursor()
        if cursor.hasSelection():
            char_format = cursor.charFormat()
            font_size = char_format.fontPointSize()
            if font_size == 0:  # Default font size
                font_size = 12
            char_format.setFontPointSize(font_size + 1)
            cursor.mergeCharFormat(char_format)
        self.textEdit.setTextCursor(cursor)

    @Slot()
    def decreaseFontSize(self):
        cursor = self.textEdit.textCursor()
        if cursor.hasSelection():
            char_format = cursor.charFormat()
            font_size = char_format.fontPointSize()
            if font_size == 0:  # Default font size
                font_size = 12
            char_format.setFontPointSize(font_size - 1)
            cursor.mergeCharFormat(char_format)
        self.textEdit.setTextCursor(cursor)

    def bind_text_edit(self, text_edit):
        self.textEdit = text_edit
        self.textEdit.textChanged.connect(self.update_content_from_view)

    @Slot()
    def update_content_from_view(self):
        if not self._is_updating:
            self._is_updating = True
            self._model.content = self.textEdit.toHtml()
            self._is_updating = False

    def initialize_content(self):
        initial_html = """
        <html>
        <head></head>
        <body>
        <p style="font-family: 'Arial'; font-size: 18pt;">Hello</p>
        <p style="font-family: 'Arial'; font-size: 12pt;">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
        </body>
        </html>
        """
        self._model.content = initial_html
