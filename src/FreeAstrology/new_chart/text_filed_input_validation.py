import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class InputDialog(QDialog):
    def __init__(self):
        super(InputDialog, self).__init__()

        self.setWindowTitle("Input Dialog")

        # Create a QLineEdit for text input
        self.text_input = QLineEdit(self)

        # Create an OK button
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.on_ok_button_clicked)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_input)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def on_ok_button_clicked(self):
        text = self.text_input.text()
        if text:
            print(f"Input Text: {text}")
        else:
            self.show_warning()

    def show_warning(self):
        warning_box = QMessageBox(self)
        warning_box.setIcon(QMessageBox.Warning)
        warning_box.setWindowTitle("Warning")
        warning_box.setText("The input field is empty.")
        warning_box.setStandardButtons(QMessageBox.Ok)
        warning_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = InputDialog()
    dialog.show()
    sys.exit(app.exec())
