import sys
import csv
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QCompleter, QMessageBox
from PySide6.QtCore import QStringListModel, Qt
import os


class SuggestionBox(QMainWindow):
    def __init__(self, csv_file):
        super(SuggestionBox, self).__init__()

        self.setWindowTitle("Search Suggestion Box")

        # Create a QLineEdit widget
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Type to search...")

        # Create a QCompleter
        self.completer = QCompleter()
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.line_edit.setCompleter(self.completer)

        # Create a QStringListModel to hold the search suggestions
        self.model = QStringListModel()
        self.completer.setModel(self.model)

        # Connect the textChanged signal to the update_completer slot
        self.line_edit.textChanged.connect(self.update_completer)

        # Load data from CSV
        self.load_data(csv_file)

        # Create a layout and add the QLineEdit widget to it
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)

    def load_data(self, csv_file):
        self.data = []
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                entry = f"{row['city_ascii']}, {row['country']}"
                self.data.append(entry)

    def update_completer(self, text):
        if text:
            # Filter data based on input text
            filtered_data = [item for item in self.data if text.lower() in item.lower()]
            self.model.setStringList(filtered_data)
        else:
            # Reset the completer if no text is entered
            self.model.setStringList([])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    relative_csv_path = "src/FreeAstrology/new_chart/worldcities.csv"  # Path to your CSV file
    csv_file = os.path.join(os.getcwd(), relative_csv_path)
    # csv_file = "FreeAstrology/new_chart/worldcities.csv"
    suggestion_box = SuggestionBox(csv_file)
    suggestion_box.show()
    sys.exit(app.exec())
