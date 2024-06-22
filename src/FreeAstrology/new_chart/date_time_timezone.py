from PySide6.QtWidgets import QApplication, QMainWindow, QDateTimeEdit, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QDateTime, Qt
import sys
import pytz
from datetime import datetime

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("QDateTimeEdit Example")

    # Create a QDateTimeEdit widget
    self.date_time_edit = QDateTimeEdit(self)
    self.date_time_edit.setCalendarPopup(True)
    self.date_time_edit.setDateTime(QDateTime.currentDateTime())

    # Create a button to print the date time in ISO format with timezone
    self.print_button = QPushButton("Print DateTime in ISO Format with Timezone", self)
    self.print_button.clicked.connect(self.print_datetime_iso)

    # Layout
    layout = QVBoxLayout()
    layout.addWidget(self.date_time_edit)
    layout.addWidget(self.print_button)

    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)

  def print_datetime_iso(self):
    # Get the date and time from QDateTimeEdit
    qt_date_time = self.date_time_edit.dateTime()

    # Convert to Python's datetime object
    py_date_time = qt_date_time.toPython()

    # Assume the local timezone for this example
    local_tz = pytz.timezone('Europe/Rome')  # You can change this to your local timezone
    local_dt = local_tz.localize(py_date_time)

    # Convert to ISO format with timezone
    iso_format = local_dt.isoformat()

    # Print to console
    print(f"ISO Format with Timezone: {iso_format}")

if __name__ == "__main__":
  app = QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  sys.exit(app.exec())
