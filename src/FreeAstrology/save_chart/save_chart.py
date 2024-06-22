from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenuBar
from PySide6.QtGui import QAction
import sys

class FileSaverWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('File Saver Example')
        self.setGeometry(100, 100, 600, 400)

        # Creare la barra dei menu
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Aggiungere il menu File
        self.file_menu = self.menu_bar.addMenu('File')

        # Aggiungere l'azione Save File al menu File
        self.save_file_action = QAction('Save File', self)
        self.file_menu.addAction(self.save_file_action)

        # Connettere l'azione Save File alla funzione save_file_dialog
        self.save_file_action.triggered.connect(self.save_file_dialog)

    def save_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)

        # Impostare i filtri per le estensioni dei file
        file_dialog.setNameFilters(["Text Files (*.txt)", "Images (*.png *.jpg *.bmp)", "All Files (*.*)"])

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            print(f'Selected file to save: {file_path}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSaverWindow()
    window.show()
    sys.exit(app.exec())
