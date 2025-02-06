# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateStudent.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMessageBox)


import mysql.connector
from random import randint
from datetime import datetime

class UpdateStudent(QDialog):

    # Define a custom signal as a class variable
    data_updated = Signal()

    def __init__(self, row_index, row_data):
        super().__init__()

        # Store the row index and row data as instance variables
        self.row_index = row_index
        self.row_data = row_data

        self.pupil_info = self.select_student()[0]

        self.student_name_info = self.pupil_info[0]
        self.student_id_info = self.pupil_info[1]
        self.student_gender_info = self.pupil_info[2]
        self.student_class_info = self.pupil_info[3]
        self.student_birthday_info = self.pupil_info[4]
        self.student_age_info = self.pupil_info[5]
        self.student_address_info = self.pupil_info[6]
        self.student_phone_info = self.pupil_info[7]
        self.student_email_info = self.pupil_info[8]

        print(self.row_data)

        self.resize(548, 584)
        self.setStyleSheet(u"QDialog{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border:1px solid gray;\n"
"	border-radius:6px;\n"
"	padding-left:15px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"	border:1px solid gray;\n"
"    border-radius:6px;\n"
"	padding-left:15px;\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 551, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(380, 167, 151, 21))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(90, 90, 90);")
        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 167, 151, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(90, 90, 90);")
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 260, 513, 67))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(90, 90, 90);")

        self.verticalLayout_2.addWidget(self.label_5)

        self.update_address_lineEdit = QLineEdit(self.layoutWidget)
        self.update_address_lineEdit.setObjectName(u"update_address_lineEdit")
        self.update_address_lineEdit.setMinimumSize(QSize(511, 31))
        self.update_address_lineEdit.setMaximumSize(QSize(511, 31))
        self.update_address_lineEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.update_address_lineEdit)

        self.layoutWidget_2 = QWidget(self)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 340, 513, 67))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(90, 90, 90);")

        self.verticalLayout_3.addWidget(self.label_6)

        self.update_phone_lineEdit = QLineEdit(self.layoutWidget_2)
        self.update_phone_lineEdit.setObjectName(u"update_phone_lineEdit")
        self.update_phone_lineEdit.setMinimumSize(QSize(511, 31))
        self.update_phone_lineEdit.setMaximumSize(QSize(511, 31))
        self.update_phone_lineEdit.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.update_phone_lineEdit)

        self.label_7 = QLabel(self)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 167, 161, 21))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(90, 90, 90);")
        self.layoutWidget_3 = QWidget(self)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 430, 513, 67))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(90, 90, 90);")

        self.verticalLayout_4.addWidget(self.label_8)

        self.update_email_lineEdit = QLineEdit(self.layoutWidget_3)
        self.update_email_lineEdit.setObjectName(u"update_email_lineEdit")
        self.update_email_lineEdit.setMinimumSize(QSize(511, 31))
        self.update_email_lineEdit.setMaximumSize(QSize(511, 31))
        self.update_email_lineEdit.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.update_email_lineEdit)

        self.updateStudent_btn = QPushButton(self)
        self.updateStudent_btn.setObjectName(u"updateStudent_btn")
        self.updateStudent_btn.setGeometry(QRect(300, 520, 141, 41))
        self.updateStudent_btn.setStyleSheet(u"background-color:#34D481;\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:15px;")
        self.update_cancel_btn = QPushButton(self)
        self.update_cancel_btn.setObjectName(u"update_cancel_btn")
        self.update_cancel_btn.setGeometry(QRect(450, 520, 81, 41))
        self.update_cancel_btn.setStyleSheet(u"background-color: #585858;\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:15px;")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 341, 31))
        font1 = QFont()
        font1.setFamilies([u"Poppins Medium"])
        font1.setPointSize(20)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(44, 44, 44);")
        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 80, 513, 67))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(90, 90, 90);")

        self.verticalLayout.addWidget(self.label_2)

        self.update_name_lineEdit = QLineEdit(self.layoutWidget1)
        self.update_name_lineEdit.setObjectName(u"update_name_lineEdit")
        self.update_name_lineEdit.setMinimumSize(QSize(511, 31))
        self.update_name_lineEdit.setMaximumSize(QSize(511, 31))
        self.update_name_lineEdit.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.update_name_lineEdit)

        self.layoutWidget2 = QWidget(self)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 200, 511, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.update_gender_comboBox = QComboBox(self.layoutWidget2)
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.setObjectName(u"update_gender_comboBox")
        self.update_gender_comboBox.setMinimumSize(QSize(0, 35))
        self.update_gender_comboBox.setStyleSheet(u" QComboBox {\n"
"                border: 2px solid #ffffff;\n"
"                border-radius: 8px;\n"
"                padding: 1px 18px 1px 3px;\n"
"                background: black;\n"
"                selection-background-color: #2980b9;\n"
"				padding-left:15px;\n"
"                color: white;\n"
"				font-weight:bold;\n"
"            }")

        self.horizontalLayout.addWidget(self.update_gender_comboBox)

        self.update_class_comboBox = QComboBox(self.layoutWidget2)
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.setObjectName(u"update_class_comboBox")
        self.update_class_comboBox.setMinimumSize(QSize(0, 35))
        self.update_class_comboBox.setStyleSheet(u" QComboBox {\n"
"                border: 2px solid #ffffff;\n"
"                border-radius: 8px;\n"
"                padding: 1px 18px 1px 3px;\n"
"                background: black;\n"
"                selection-background-color: #2980b9;\n"
"				padding-left:15px;\n"
"                color: white;\n"
"				font-weight:bold;\n"
"            }")

        self.horizontalLayout.addWidget(self.update_class_comboBox)

        self.update_dob_dateEdit = QDateEdit(self.layoutWidget2)
        self.update_dob_dateEdit.setObjectName(u"update_dob_dateEdit")
        self.update_dob_dateEdit.setMinimumSize(QSize(0, 31))

        self.horizontalLayout.addWidget(self.update_dob_dateEdit)
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("UpdateStudent", u"Update Student Dialog", None))
        self.setWindowIcon(QIcon(":/Icons/logo.png"))
        self.label_3.setText(QCoreApplication.translate("UpdateStudent", u"Date Of Birth", None))
        self.label_4.setText(QCoreApplication.translate("UpdateStudent", u"Class", None))
        self.label_5.setText(QCoreApplication.translate("UpdateStudent", u"Address", None))
        self.label_6.setText(QCoreApplication.translate("UpdateStudent", u"Phone Number", None))
        self.label_7.setText(QCoreApplication.translate("UpdateStudent", u"Gender", None))
        self.label_8.setText(QCoreApplication.translate("UpdateStudent", u"Email", None))
        self.updateStudent_btn.setText(QCoreApplication.translate("UpdateStudent", u"Update Student", None))
        self.update_cancel_btn.setText(QCoreApplication.translate("UpdateStudent", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("UpdateStudent", u"Update Student Info", None))
        self.label_2.setText(QCoreApplication.translate("UpdateStudent", u"Full Names", None))
        self.update_gender_comboBox.setItemText(0, QCoreApplication.translate("UpdateStudent", u"Male", None))
        self.update_gender_comboBox.setItemText(1, QCoreApplication.translate("UpdateStudent", u"Female", None))

        self.update_class_comboBox.setItemText(0, QCoreApplication.translate("UpdateStudent", u"Select Class", None))
        self.update_class_comboBox.setItemText(1, QCoreApplication.translate("UpdateStudent", u"Grade 1", None))
        self.update_class_comboBox.setItemText(2, QCoreApplication.translate("UpdateStudent", u"Grade 2", None))
        self.update_class_comboBox.setItemText(3, QCoreApplication.translate("UpdateStudent", u"Grade 3", None))
        self.update_class_comboBox.setItemText(4, QCoreApplication.translate("UpdateStudent", u"Grade 4", None))
        self.update_class_comboBox.setItemText(5, QCoreApplication.translate("UpdateStudent", u"Grade 5", None))
        self.update_class_comboBox.setItemText(6, QCoreApplication.translate("UpdateStudent", u"Grade 6", None))
        self.update_class_comboBox.setItemText(7, QCoreApplication.translate("UpdateStudent", u"Grade 7", None))
        self.update_class_comboBox.setItemText(8, QCoreApplication.translate("UpdateStudent", u"Grade 8", None))
        self.update_class_comboBox.setItemText(9, QCoreApplication.translate("UpdateStudent", u"Grade 9", None))
        self.update_class_comboBox.setItemText(10, QCoreApplication.translate("UpdateStudent", u"Grade 10", None))
        self.update_class_comboBox.setItemText(11, QCoreApplication.translate("UpdateStudent", u"Grade 11", None))
        self.update_class_comboBox.setItemText(12, QCoreApplication.translate("UpdateStudent", u"Grade 12", None))

    # retranslateUi

        # Convert the string to a QDate and set it in the QDateEdit
        date_object = QDate.fromString(self.student_birthday_info, "yyyy-MM-dd")
        
        self.update_name_lineEdit.setText(str(self.student_name_info))
        self.update_gender_comboBox.setCurrentText(str(self.student_gender_info))
        self.update_class_comboBox.setCurrentText(str(self.student_class_info))
        self.update_dob_dateEdit.setDate(date_object)
        self.update_address_lineEdit.setText(str(self.student_address_info))
        self.update_phone_lineEdit.setText(str(self.student_phone_info))
        self.update_email_lineEdit.setText(str(self.student_email_info))

        # Get gender index
        self.lastIndex = self.update_gender_comboBox.currentText()
        print("Last index version 1", self.lastIndex)

        self.updateStudent_btn.clicked.connect(self.update_data)

################################################################################
## 
##
## CREATE DATABASE CONNECTION
##
## 
################################################################################

    def create_connection(self):

        # Replace these with your actual MySQL server details
        host_name = "localhost"
        user_name = "root"
        mypassword = ""
        database_name = "atepi_school"

        # Establish a connection to MySQL server
        self.mydb = mysql.connector.connect(
                host= host_name,
                user= user_name,
                password= mypassword,
                database = database_name,
            )
        
        # Create a cursor to execute SQL queries
        cursor = self.mydb.cursor()

        #Create the database if it doesn't exist
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')

        return self.mydb
    
    def select_student(self):

        self.cursor = self.create_connection().cursor()

        #Get pupil variables from tuple
        self.student_name = self.row_data[0]
        self.student_id = self.row_data[1]

        params = [
            self.student_name,
            self.student_id,
        ]

        select_query = f"SELECT * FROM students_table WHERE names=%s AND student_id=%s"
 
        self.cursor.execute(select_query, params)

        records = self.cursor.fetchall()

        self.mydb.commit()
        self.mydb.close
        return records
    
    def update_data(self):

        try:
            connection = self.create_connection()
            if connection is None:
                return
            
            cursor = connection.cursor()

            # Assuming birth_date is a QDate object
            birth_date = self.update_dob_dateEdit.date()

            birthday = self.handleDateChange()
            age = self.calculate_age(birth_date)
            print(age)

            # Check if gender has changed and generate new student ID if needed
            current_student_id = self.on_gender_index_changed(self.update_gender_comboBox.currentText())

            #Find the number of rows in the list results[0]
            params = (
                self.update_name_lineEdit.text(),
                current_student_id,
                self.update_gender_comboBox.currentText(),
                self.update_class_comboBox.currentText(),
                birthday,
                age,
                self.update_address_lineEdit.text(),
                self.update_phone_lineEdit.text(),
                self.update_email_lineEdit.text(),
                self.student_id_info,
            )

            print(params)

            update_query = f"UPDATE students_table SET names=%s , student_id=%s, gender=%s, class=%s, birthday=%s, age=%s, address=%s, phone_number=%s, email=%s  WHERE student_id=%s"

            cursor.execute(update_query, params)
            connection.commit()
            self.show_updated_message()
            cursor.close()
            connection.close()
            self.close()

            # Emit the signal
            self.data_updated.emit()


        except mysql.connector.Error as err:
            # Handle MySQL errors
            print(f"Error: {err}")
    
    def handleDateChange(self):
        # Convert QDate to a string in the format 'YYYY-MM-DD'
        selected_date = self.update_dob_dateEdit.date()
        self.date_string = selected_date.toString(Qt.ISODate)

        return self.date_string
    
    def calculate_age(self, birth_date):
        # Get the current date
        current_date = datetime.now().date()

        # Create a date object for the birthdate
        birth_datetime = datetime(birth_date.year(), birth_date.month(), birth_date.day()).date()

        # Calculate the difference in years
        age = current_date.year - birth_datetime.year

        # Check if the birthday has occurred this year
        if (current_date.month, current_date.day) < (birth_datetime.month, birth_datetime.day):
            age -= 1

        return age
    
    def on_gender_index_changed(self, index):

        if index != self.lastIndex:
            gender_item = self.update_gender_comboBox.currentText()
            new_student_id = self.generate_studentId(gender_item)
            
            return new_student_id
        else:
            return self.student_id_info

    def generate_studentId(self, gender):

        if gender == "Male":
            id_start_value = "24" + "/U/M"
        else:
            id_start_value = "24" + "/U/F"

        random_value = self.generate_randomNumber()
        student_id = id_start_value + random_value
            
        return student_id

    def generate_randomNumber(self):
        number = randint(1, 1000)
        random_number = f"{number:04d}"
        return random_number
    
    def show_updated_message(self):
        # Show a message box with a green tick
        msg_box = QMessageBox(self)
        #msg_box.setIconPixmap(QPixmap('green_tick.png'))  # Replace 'green_tick.png' with the path to your green tick image
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.student_name_info + " information updated successfully.")
        msg_box.exec()