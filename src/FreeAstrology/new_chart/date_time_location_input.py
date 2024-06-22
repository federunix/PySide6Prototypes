import sys
import csv
from datetime import datetime
from timezonefinder import TimezoneFinder
from pytz import timezone, utc
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QDateTimeEdit,
                               QPushButton, QDialog, QCalendarWidget, QLineEdit, QLabel)
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
        self.city_data = self.load_city_data(
            '/home/fede/Documents/Software/VSCode/FreeAstrology/PySidePrototypes/src/date/worldcities.csv')

    def initUI(self):
        self.setWindowTitle('Date Time Input Example')
        self.setGeometry(100, 100, 600, 400)

        self.date_time_edit = QDateTimeEdit(self)
        self.date_time_edit.setCalendarPopup(True)
        self.date_time_edit.setDateTime(QDateTime.currentDateTime())
        self.date_time_edit.setDisplayFormat('dd/MM/yyyy HH:mm:ss')

        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText('Enter city name')

        search_button = QPushButton('Search', self)
        search_button.clicked.connect(self.search_city)

        self.result_label = QLabel('', self)

        ok_button = QPushButton('OK', self)
        ok_button.clicked.connect(self.print_datetime)

        layout = QVBoxLayout()
        layout.addWidget(self.date_time_edit)
        layout.addWidget(self.city_input)
        layout.addWidget(search_button)
        layout.addWidget(self.result_label)
        layout.addWidget(ok_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def load_city_data(self, filename):
        city_data = {}
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                city = row['city_ascii']
                lat = float(row['lat'])
                lng = float(row['lng'])
                city_data[city] = {'lat': lat, 'lng': lng}
        return city_data

    def search_city(self):
        city_name = self.city_input.text()
        if not city_name:
            self.result_label.setText('Please enter a city name.')
            return

        city_info = self.city_data.get(city_name)
        if city_info:
            lat = city_info['lat']
            lng = city_info['lng']
            tf = TimezoneFinder()
            tz_name = tf.timezone_at(lng=lng, lat=lat)
            self.result_label.setText(
                f'Coordinates: {lat}, {lng} - Timezone: {tz_name}')
            self.city_timezone = tz_name
        else:
            self.result_label.setText('City not found.')

    def print_datetime(self):
        datetime = self.date_time_edit.dateTime()
        if hasattr(self, 'city_timezone'):
            local_tz = timezone(self.city_timezone)
            local_dt = local_tz.localize(datetime.toPyDateTime())
            print(local_dt.isoformat())
        else:
            print(datetime.toString(Qt.ISODate))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
