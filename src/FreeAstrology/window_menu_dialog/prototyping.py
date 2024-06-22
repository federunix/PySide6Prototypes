import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLineEdit, QPushButton, QDialogButtonBox
from PySide6.QtCore import QMetaObject
from PySide6.QtGui import QIcon, QAction


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(30, 240, 341, 32)
        # self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(100, 110, 113, 23)

        # self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # def retranslateUi(self, Dialog):
    #     Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.print_content)
        self.ui.buttonBox.rejected.connect(self.close_dialog)

    def print_content(self):
        content = self.ui.lineEdit.text()
        print("Submitted content:", content)
        self.close()

    def close_dialog(self):
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Main Window")

        # Create menu bar
        self.menu_bar = self.menuBar()

        # Create File menu and add actions
        file_menu = self.menu_bar.addMenu("File")

        # Create New dialog action
        new_dialog_action = QAction("Open Dialog", self)
        new_dialog_action.triggered.connect(self.open_dialog)
        file_menu.addAction(new_dialog_action)

    def open_dialog(self):
        dialog = Dialog(self)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
