# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewChart.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QSplitter, QTextEdit, QWidget)

class Ui_NewChart(object):
    def setupUi(self, NewChart):
        self.NewChartNameInput = QTextEdit(NewChart)
        self.NewChartNameInput.setObjectName(u"NewChartNameInput")
        self.NewChartNameInput.setGeometry(QRect(70, 20, 104, 31))
        self.NewChartDayInput = QTextEdit(NewChart)
        self.NewChartDayInput.setObjectName(u"NewChartDayInput")
        self.NewChartDayInput.setGeometry(QRect(50, 100, 41, 31))
        self.NewChartMonthInput = QTextEdit(NewChart)
        self.NewChartMonthInput.setObjectName(u"NewChartMonthInput")
        self.NewChartMonthInput.setGeometry(QRect(110, 100, 41, 31))
        self.NewChartYearInput = QTextEdit(NewChart)
        self.NewChartYearInput.setObjectName(u"NewChartYearInput")
        self.NewChartYearInput.setGeometry(QRect(170, 100, 61, 31))
        self.NewChartHourInput = QTextEdit(NewChart)
        self.NewChartHourInput.setObjectName(u"NewChartHourInput")
        self.NewChartHourInput.setGeometry(QRect(290, 100, 41, 31))
        self.NewChartMinuteInput = QTextEdit(NewChart)
        self.NewChartMinuteInput.setObjectName(u"NewChartMinuteInput")
        self.NewChartMinuteInput.setGeometry(QRect(350, 100, 41, 31))
        self.NewChartSecondInput = QTextEdit(NewChart)
        self.NewChartSecondInput.setObjectName(u"NewChartSecondInput")
        self.NewChartSecondInput.setGeometry(QRect(410, 100, 41, 31))
        self.label_Name = QLabel(NewChart)
        self.label_Name.setObjectName(u"label_Name")
        self.label_Name.setGeometry(QRect(10, 20, 62, 16))
        self.label_Day = QLabel(NewChart)
        self.label_Day.setObjectName(u"label_Day")
        self.label_Day.setGeometry(QRect(20, 80, 62, 16))
        self.label_Month = QLabel(NewChart)
        self.label_Month.setObjectName(u"label_Month")
        self.label_Month.setGeometry(QRect(90, 80, 62, 16))
        self.label_Year = QLabel(NewChart)
        self.label_Year.setObjectName(u"label_Year")
        self.label_Year.setGeometry(QRect(150, 80, 62, 16))
        self.label_Hour = QLabel(NewChart)
        self.label_Hour.setObjectName(u"label_Hour")
        self.label_Hour.setGeometry(QRect(270, 80, 62, 16))
        self.label_Minute = QLabel(NewChart)
        self.label_Minute.setObjectName(u"label_Minute")
        self.label_Minute.setGeometry(QRect(330, 80, 62, 16))
        self.label_Second = QLabel(NewChart)
        self.label_Second.setObjectName(u"label_Second")
        self.label_Second.setGeometry(QRect(400, 80, 62, 16))
        self.label_Surname = QLabel(NewChart)
        self.label_Surname.setObjectName(u"label_Surname")
        self.label_Surname.setGeometry(QRect(230, 30, 62, 16))
        self.NewChartSurnameInput = QTextEdit(NewChart)
        self.NewChartSurnameInput.setObjectName(u"NewChartSurnameInput")
        self.NewChartSurnameInput.setGeometry(QRect(320, 20, 104, 31))
        self.NewChartSearchInput = QTextEdit(NewChart)
        self.NewChartSearchInput.setObjectName(u"NewChartSearchInput")
        self.NewChartSearchInput.setGeometry(QRect(140, 180, 104, 31))
        self.NewChartSearchButton = QPushButton(NewChart)
        self.NewChartSearchButton.setObjectName(u"NewChartSearchButton")
        self.NewChartSearchButton.setGeometry(QRect(280, 180, 80, 24))
        self.label_SearchCity = QLabel(NewChart)
        self.label_SearchCity.setObjectName(u"label_SearchCity")
        self.label_SearchCity.setGeometry(QRect(20, 190, 91, 16))
        self.splitter = QSplitter(NewChart)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(40, 270, 357, 24))
        self.splitter.setOrientation(Qt.Horizontal)
        self.NewChartAddDataBaseButton = QPushButton(self.splitter)
        self.NewChartAddDataBaseButton.setObjectName(u"NewChartAddDataBaseButton")
        self.splitter.addWidget(self.NewChartAddDataBaseButton)
        self.NewChartTestButton = QPushButton(self.splitter)
        self.NewChartTestButton.setObjectName(u"NewChartTestButton")
        self.splitter.addWidget(self.NewChartTestButton)
        self.NewChartCancelButton = QPushButton(self.splitter)
        self.NewChartCancelButton.setObjectName(u"NewChartCancelButton")
        self.splitter.addWidget(self.NewChartCancelButton)
        self.NewChartOKButton = QPushButton(self.splitter)
        self.NewChartOKButton.setObjectName(u"NewChartOKButton")
        self.splitter.addWidget(self.NewChartOKButton)

        self.retranslateUi(NewChart)

        QMetaObject.connectSlotsByName(NewChart)
    # setupUi

    def retranslateUi(self, NewChart):
        NewChart.setWindowTitle(QCoreApplication.translate("NewChart", u"Dialog", None))
        self.NewChartDayInput.setPlaceholderText(QCoreApplication.translate("NewChart", u"01", None))
        self.NewChartMonthInput.setPlaceholderText(QCoreApplication.translate("NewChart", u"01", None))
        self.NewChartYearInput.setPlaceholderText(QCoreApplication.translate("NewChart", u"1970", None))
        self.NewChartHourInput.setPlaceholderText(QCoreApplication.translate("NewChart", u"00", None))
        self.NewChartMinuteInput.setPlaceholderText(QCoreApplication.translate("NewChart", u"00", None))
        self.NewChartSecondInput.setPlaceholderText(QCoreApplication.translate("NewChart", u"00", None))
        self.label_Name.setText(QCoreApplication.translate("NewChart", u"Name", None))
        self.label_Day.setText(QCoreApplication.translate("NewChart", u"Day", None))
        self.label_Month.setText(QCoreApplication.translate("NewChart", u"Month", None))
        self.label_Year.setText(QCoreApplication.translate("NewChart", u"Year", None))
        self.label_Hour.setText(QCoreApplication.translate("NewChart", u"Hour", None))
        self.label_Minute.setText(QCoreApplication.translate("NewChart", u"Minute", None))
        self.label_Second.setText(QCoreApplication.translate("NewChart", u"Second", None))
        self.label_Surname.setText(QCoreApplication.translate("NewChart", u"Surname", None))
        self.NewChartSearchButton.setText(QCoreApplication.translate("NewChart", u"Search", None))
        self.label_SearchCity.setText(QCoreApplication.translate("NewChart", u"Search City", None))
        self.NewChartAddDataBaseButton.setText(QCoreApplication.translate("NewChart", u"Add to Database", None))
        self.NewChartTestButton.setText(QCoreApplication.translate("NewChart", u"Test", None))
        self.NewChartCancelButton.setText(QCoreApplication.translate("NewChart", u"Cancel", None))
        self.NewChartOKButton.setText(QCoreApplication.translate("NewChart", u"OK", None))
    # retranslateUi
