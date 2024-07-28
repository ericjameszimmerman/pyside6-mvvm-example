import qtawesome as qta
from PySide6.QtCore import Qt, QStringListModel, QModelIndex
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QSplitter, QListView, QVBoxLayout,
    QLabel, QWidget, QToolBar, QStatusBar, QMenuBar, QHBoxLayout, QMessageBox, QStackedWidget
)
import sys
import model
import view
import viewmodel
from view.widget import IconLabel


class MainWindow(QMainWindow):
    def __init__(self, theme):
        super().__init__()

        self.setWindowTitle("MVVM Example with PySide6")
        self.resize(800, 600)
        self.theme = theme
        icon_color = self.theme.default_text_color

        # Create the QStackedWidget to hold the views
        self.stacked_widget = QStackedWidget()
        self.view_lookup = {}

        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QHBoxLayout(self)
        
        # List Model
        self.items = [
            model.ItemModel("Drive Simulator", "icons/fruit.png", "simulator"),
            model.ItemModel("Item 2", "icons/flag.png", "dummy1"),
            model.ItemModel("Item 3", "icons/hamburger.png", "dummy2")
        ]
        self.view_models = [viewmodel.ItemViewModel(item) for item in self.items]
        self.model = QStringListModel([vm.get_name() for vm in self.view_models])
        
        # Left Pane: List View
        self.left_pane_view = view.LeftPaneView()
        self.left_pane_view.setModel(self.model)
        main_layout.addWidget(self.left_pane_view)

        self.initialize_views()

        main_layout.addWidget(self.stacked_widget)
        central_widget.setLayout(main_layout)

        # Create the menu bar
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("File")

        new_action = QAction(qta.icon('fa5s.file', color=icon_color), "New", self)
        new_action.setShortcut("Ctrl+N")
        open_action = QAction(qta.icon('fa5s.folder-open', color=icon_color), "Open", self)
        open_action.setShortcut("Ctrl+O")
        save_action = QAction(qta.icon('fa5s.save', color=icon_color), "Save", self)
        save_action.setShortcut("Ctrl+S")
        save_as_action = QAction(qta.icon('fa5s.save', color=icon_color), "Save As", self)
        exit_action = QAction(qta.icon('fa5s.sign-out-alt', color=icon_color), "Exit", self)
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

        undo_action = QAction(qta.icon('fa5s.undo', color=icon_color), "Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        redo_action = QAction(qta.icon('fa5s.redo', color=icon_color), "Redo", self)
        redo_action.setShortcut("Ctrl+Y")
        cut_action = QAction(qta.icon('fa5s.cut', color=icon_color), "Cut", self)
        cut_action.setShortcut("Ctrl+X")
        copy_action = QAction(qta.icon('fa5s.copy', color=icon_color), "Copy", self)
        copy_action.setShortcut("Ctrl+C")
        paste_action = QAction(qta.icon('fa5s.paste', color=icon_color), "Paste", self)
        paste_action.setShortcut("Ctrl+V")

        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)

        # Settings Menu
        settings_menu = menu_bar.addMenu("Settings")

        preferences_action = QAction(qta.icon('fa5s.cog', color=icon_color), "Preferences", self)
        preferences_action.triggered.connect(self.show_settings_dialog)

        settings_menu.addAction(preferences_action)

        # Help Menu
        help_menu = menu_bar.addMenu("Help")

        about_action = QAction(qta.icon('fa5s.info-circle', color=icon_color), "About", self)
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

    def initialize_views(self):
        self.drive_model = model.MotorDriveModel()
        drive_viewmodel = viewmodel.MotorDriveViewModel(self.drive_model)
        simulator = view.MotorDriveView(drive_viewmodel)
        self.view_lookup["simulator"] = simulator
        self.stacked_widget.addWidget(simulator)

        self.dummy1 = model.DummyModel()
        self.dummy1.data = "Eric is Cool"
        dummy1_viewmodel = viewmodel.DummyViewModel(self.dummy1)
        dummy1_view = view.DummyView(dummy1_viewmodel)
        self.view_lookup["dummy1"] = dummy1_view
        self.stacked_widget.addWidget(dummy1_view)

        self.dummy2 = model.DummyModel()
        self.dummy2.data = "Dummy 2"
        dummy2_viewmodel = viewmodel.DummyViewModel(self.dummy2)
        dummy2_view = view.DummyView(dummy2_viewmodel)
        self.view_lookup["dummy2"] = dummy2_view
        self.stacked_widget.addWidget(dummy2_view)

    def show_about_dialog(self):
        QMessageBox.about(self, "About", "This is a sample application with a menu bar created using PySide6.")

    def show_settings_dialog(self):
        settings = model.SettingsModel()
        view_model = viewmodel.SettingsViewModel(settings)
        dialog = view.SettingsDialog(view_model)
        dialog.exec()

    def on_item_selected(self, current: QModelIndex, previous: QModelIndex):
        index = current.row()
        selected_view_model = self.view_models[index]
        if selected_view_model:
            view_id = selected_view_model.get_view_id()
            view_ref = self.view_lookup[view_id]
            if view_ref:
                self.stacked_widget.setCurrentWidget(view_ref)
            self.status_bar.showMessage(f"Selected {selected_view_model.get_name()}")

    def update_icons(self):
        for index, view_model in enumerate(self.view_models):
            icon = QIcon(view_model.get_icon_path())
            self.left_pane_view.setIndexWidget(self.model.index(index, 0), IconLabel("fa.scissors", "Slicer Limit:"))

    def on_about_to_quit(self):
        self.drive_model.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    #theme = view.themes.DarkTheme(app)
    theme = view.themes.LightTheme(app)
    window = MainWindow(theme)
    app.aboutToQuit.connect(window.on_about_to_quit)
    window.show()
    theme.apply()
    sys.exit(app.exec())
