import sys
import locale
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDateTimeEdit, QPushButton, QDialog, QCalendarWidget
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QDateTime, QSize, Qt

class CalendarDialog(QDialog):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle('Select Date and Time')

    self.calendar = QCalendarWidget(self)
    self.calendar.setGridVisible(True)
    self.calendar.clicked.connect(self.accept)

    layout = QVBoxLayout()
    layout.addWidget(self.calendar)
    self.setLayout(layout)

  def getSelectedDate(self):
    return self.calendar.selectedDate()

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setWindowTitle('Date Time Input Example')

    self.date_time_edit = QDateTimeEdit(self)
    self.date_time_edit.setCalendarPopup(True)
    self.date_time_edit.setDateTime(QDateTime.currentDateTime())
    self.date_time_edit.setDisplayFormat('dd/MM/yyyy HH:mm:ss')

    calendar_button = QPushButton(self)
    calendar_button.setIcon(QIcon(QPixmap('calendar_icon.png')))
    calendar_button.setIconSize(QSize(32, 32))
    calendar_button.clicked.connect(self.open_calendar_dialog)

    ok_button = QPushButton('OK', self)
    ok_button.clicked.connect(self.print_datetime)

    layout = QVBoxLayout()
    layout.addWidget(self.date_time_edit)
    layout.addWidget(calendar_button)
    layout.addWidget(ok_button)

    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)

  def open_calendar_dialog(self):
    dialog = CalendarDialog()
    if dialog.exec():
      selected_date = dialog.getSelectedDate()
      self.date_time_edit.setDate(selected_date)

  def print_datetime(self):
    datetime = self.date_time_edit.dateTime()
    print(datetime.toString(Qt.ISODate))

if __name__ == '__main__':
  app = QApplication(sys.argv)
  main_win = MainWindow()
  main_win.show()
  sys.exit(app.exec())
