from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenuBar
from PySide6.QtGui import QAction
import sys

class FileSelectorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('File Selector Example')
        self.setGeometry(100, 100, 600, 400)

        # Creare la barra dei menu
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Aggiungere il menu File
        self.file_menu = self.menu_bar.addMenu('File')

        # Aggiungere l'azione Open File al menu File
        self.open_file_action = QAction('Open File', self)
        self.file_menu.addAction(self.open_file_action)

        # Connettere l'azione Open File alla funzione open_file_dialog
        self.open_file_action.triggered.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilters(["Free Astrology Files (*.xfl)", "All Files (*.*)"])

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            print(f'Selected file: {file_path}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSelectorWindow()
    window.show()
    sys.exit(app.exec())
