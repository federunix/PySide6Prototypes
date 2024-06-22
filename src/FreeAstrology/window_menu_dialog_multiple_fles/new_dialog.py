import sys
from PySide6.QtWidgets import QApplication, QDialog

# Import the generated UI class
from NewChartUI import Ui_NewChart

class NewChartDialog(QDialog):
    def __init__(self):
        super(NewChartDialog, self).__init__()
        self.ui = Ui_NewChart()
        self.ui.setupUi(self)

        # Connect the buttons to their respective methods
        self.ui.NewChartOKButton.clicked.connect(self.ok_button_clicked)
        self.ui.NewChartCancelButton.clicked.connect(self.cancel_button_clicked)
        self.ui.NewChartAddDataBaseButton.clicked.connect(self.add_to_database)
        self.ui.NewChartTestButton.clicked.connect(self.test_button_clicked)
        self.ui.NewChartSearchButton.clicked.connect(self.search_city)

    def ok_button_clicked(self):
        print("OK button clicked")
        self.accept()

    def cancel_button_clicked(self):
        print("Cancel button clicked")
        self.reject()

    def add_to_database(self):
        print("Add to Database button clicked")
        # Implement the logic to add data to the database here

    def test_button_clicked(self):
        print("Test button clicked")
        # Implement the logic to test the input data here

    def search_city(self):
        city_name = self.ui.NewChartSearchInput.toPlainText()
        print(f"Searching for city: {city_name}")
        # Implement the logic to search for the city here

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = NewChartDialog()
    dialog.show()

    sys.exit(app.exec())
