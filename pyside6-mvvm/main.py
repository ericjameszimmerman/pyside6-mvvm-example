import qtawesome as qta
from PySide6.QtCore import Qt, QStringListModel, QModelIndex
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QSplitter, QListView, QVBoxLayout,
    QLabel, QWidget, QToolBar, QStatusBar, QMenuBar, QHBoxLayout, QMessageBox
)
import sys
import model
import view
import viewmodel
from view.widget import IconLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MVVM Example with PySide6")
        self.resize(800, 600)
        self.icon_color = "white"

        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QHBoxLayout(self)
        
        # List Model
        self.items = [
            model.ItemModel("Item 1", "icons/fruit.png"),
            model.ItemModel("Item 2", "icons/flag.png"),
            model.ItemModel("Item 3", "icons/hamburger.png")
        ]
        self.view_models = [viewmodel.ItemViewModel(item) for item in self.items]
        self.model = QStringListModel([vm.get_name() for vm in self.view_models])
        
        # Left Pane: List View
        self.left_pane_view = view.LeftPaneView()
        self.left_pane_view.setModel(self.model)
        main_layout.addWidget(self.left_pane_view)

        # Right Pane: Content Area
        self.content_view = view.ContentView()
        main_layout.addWidget(self.content_view)

        central_widget.setLayout(main_layout)

        # Create the menu bar
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("File")

        new_action = QAction(qta.icon('fa5s.file', color=self.icon_color), "New", self)
        new_action.setShortcut("Ctrl+N")
        open_action = QAction(qta.icon('fa5s.folder-open', color=self.icon_color), "Open", self)
        open_action.setShortcut("Ctrl+O")
        save_action = QAction(qta.icon('fa5s.save', color=self.icon_color), "Save", self)
        save_action.setShortcut("Ctrl+S")
        save_as_action = QAction(qta.icon('fa5s.save', color=self.icon_color), "Save As", self)
        exit_action = QAction(qta.icon('fa5s.sign-out-alt', color=self.icon_color), "Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # Edit Menu
        edit_menu = menu_bar.addMenu("Edit")

        undo_action = QAction(qta.icon('fa5s.undo', color=self.icon_color), "Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        redo_action = QAction(qta.icon('fa5s.redo', color=self.icon_color), "Redo", self)
        redo_action.setShortcut("Ctrl+Y")
        cut_action = QAction(qta.icon('fa5s.cut', color=self.icon_color), "Cut", self)
        cut_action.setShortcut("Ctrl+X")
        copy_action = QAction(qta.icon('fa5s.copy', color=self.icon_color), "Copy", self)
        copy_action.setShortcut("Ctrl+C")
        paste_action = QAction(qta.icon('fa5s.paste', color=self.icon_color), "Paste", self)
        paste_action.setShortcut("Ctrl+V")

        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)

        # Settings Menu
        settings_menu = menu_bar.addMenu("Settings")

        preferences_action = QAction(qta.icon('fa5s.cog', color=self.icon_color), "Preferences", self)

        settings_menu.addAction(preferences_action)

        # Help Menu
        help_menu = menu_bar.addMenu("Help")

        about_action = QAction(qta.icon('fa5s.info-circle', color=self.icon_color), "About", self)
        about_action.triggered.connect(self.show_about_dialog)

        help_menu.addAction(about_action)

        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)  # Prevent the toolbar from being moved
        self.addToolBar(toolbar)
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)
        toolbar.addSeparator()
        toolbar.addAction(cut_action)
        toolbar.addAction(copy_action)
        toolbar.addAction(paste_action)

        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Connect selection change signal to the view model
        self.left_pane_view.selectionModel().currentChanged.connect(self.on_item_selected)

        # Set icons for list items
        self.update_icons()

        # Initialize the right pane with the first item's content
        self.left_pane_view.setCurrentIndex(self.model.index(0, 0))

    def show_about_dialog(self):
        QMessageBox.about(self, "About", "This is a sample application with a menu bar created using PySide6.")

    def on_item_selected(self, current: QModelIndex, previous: QModelIndex):
        index = current.row()
        self.content_view.display_content(self.view_models[index].get_content())
        self.status_bar.showMessage(f"Selected {self.view_models[index].get_name()}")

    def update_icons(self):
        for index, view_model in enumerate(self.view_models):
            icon = QIcon(view_model.get_icon_path())
            self.left_pane_view.setIndexWidget(self.model.index(index, 0), IconLabel("fa.scissors", "Slicer Limit:"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    theme = view.themes.DarkTheme(app)
    window = MainWindow()
    window.show()
    theme.apply()
    sys.exit(app.exec())
