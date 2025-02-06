from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
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

class Ui_StudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

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

        self.address_lineEdit = QLineEdit(self.layoutWidget)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setMinimumSize(QSize(511, 31))
        self.address_lineEdit.setMaximumSize(QSize(511, 31))
        self.address_lineEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.address_lineEdit)

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

        self.phone_lineEdit = QLineEdit(self.layoutWidget_2)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setMinimumSize(QSize(511, 31))
        self.phone_lineEdit.setMaximumSize(QSize(511, 31))
        self.phone_lineEdit.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.phone_lineEdit)

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

        self.email_lineEdit = QLineEdit(self.layoutWidget_3)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(511, 31))
        self.email_lineEdit.setMaximumSize(QSize(511, 31))
        self.email_lineEdit.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.email_lineEdit)

        self.saveStudent_btn = QPushButton(self)
        self.saveStudent_btn.setObjectName(u"saveStudent_btn")
        self.saveStudent_btn.setGeometry(QRect(320, 520, 121, 41))
        self.saveStudent_btn.setStyleSheet(u"background-color:#00E159;\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:15px;")
        self.cancel_btn = QPushButton(self)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(450, 520, 81, 41))
        self.cancel_btn.setStyleSheet(u"background-color: #585858;\n"
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

        self.name_lineEdit = QLineEdit(self.layoutWidget1)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(511, 31))
        self.name_lineEdit.setMaximumSize(QSize(511, 31))
        self.name_lineEdit.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.name_lineEdit)

        self.layoutWidget2 = QWidget(self)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 200, 511, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gender_comboBox = QComboBox(self.layoutWidget2)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setMinimumSize(QSize(0, 35))
        self.gender_comboBox.setStyleSheet(u" QComboBox {\n"
"                border: 2px solid #ffffff;\n"
"                border-radius: 8px;\n"
"                padding: 1px 18px 1px 3px;\n"
"                background: black;\n"
"                selection-background-color: #2980b9;\n"
"				padding-left:15px;\n"
"                color: white;\n"
"				font-weight:bold;\n"
"            }")

        self.horizontalLayout.addWidget(self.gender_comboBox)

        self.class_comboBox = QComboBox(self.layoutWidget2)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")
        self.class_comboBox.setMinimumSize(QSize(0, 35))
        self.class_comboBox.setStyleSheet(u" QComboBox {\n"
"                border: 2px solid #ffffff;\n"
"                border-radius: 8px;\n"
"                padding: 1px 18px 1px 3px;\n"
"                background: black;\n"
"                selection-background-color: #2980b9;\n"
"				padding-left:15px;\n"
"                color: white;\n"
"				font-weight:bold;\n"
"            }")

        self.horizontalLayout.addWidget(self.class_comboBox)

        self.dob_dateEdit = QDateEdit(self.layoutWidget2)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")
        self.dob_dateEdit.setMinimumSize(QSize(0, 31))

        self.horizontalLayout.addWidget(self.dob_dateEdit)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, StudentDialog):
        StudentDialog.setWindowTitle(QCoreApplication.translate("StudentDialog", u"Add Student Dialog", None))
        self.setWindowIcon(QIcon(":/Icons/logo.png"))
        self.label_3.setText(QCoreApplication.translate("StudentDialog", u"Date Of Birth", None))
        self.label_4.setText(QCoreApplication.translate("StudentDialog", u"Class", None))
        self.label_5.setText(QCoreApplication.translate("StudentDialog", u"Address", None))
        self.label_6.setText(QCoreApplication.translate("StudentDialog", u"Phone Number", None))
        self.label_7.setText(QCoreApplication.translate("StudentDialog", u"Gender", None))
        self.label_8.setText(QCoreApplication.translate("StudentDialog", u"Email", None))
        self.saveStudent_btn.setText(QCoreApplication.translate("StudentDialog", u"Add Student", None))
        self.cancel_btn.setText(QCoreApplication.translate("StudentDialog", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("StudentDialog", u"Add New Student", None))
        self.label_2.setText(QCoreApplication.translate("StudentDialog", u"Full Names", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentDialog", u"Select Gender", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentDialog", u"Male", None))
        self.gender_comboBox.setItemText(2, QCoreApplication.translate("StudentDialog", u"Female", None))

        self.class_comboBox.setItemText(0, QCoreApplication.translate("StudentDialog", u"Select Class", None))
        self.class_comboBox.setItemText(1, QCoreApplication.translate("StudentDialog", u"Grade 1", None))
        self.class_comboBox.setItemText(2, QCoreApplication.translate("StudentDialog", u"Grade 2", None))
        self.class_comboBox.setItemText(3, QCoreApplication.translate("StudentDialog", u"Grade 3", None))
        self.class_comboBox.setItemText(4, QCoreApplication.translate("StudentDialog", u"Grade 4", None))
        self.class_comboBox.setItemText(5, QCoreApplication.translate("StudentDialog", u"Grade 5", None))
        self.class_comboBox.setItemText(6, QCoreApplication.translate("StudentDialog", u"Grade 6", None))
        self.class_comboBox.setItemText(7, QCoreApplication.translate("StudentDialog", u"Grade 7", None))
        self.class_comboBox.setItemText(8, QCoreApplication.translate("StudentDialog", u"Grade 8", None))
        self.class_comboBox.setItemText(9, QCoreApplication.translate("StudentDialog", u"Grade 9", None))
        self.class_comboBox.setItemText(10, QCoreApplication.translate("StudentDialog", u"Grade 10", None))
        self.class_comboBox.setItemText(11, QCoreApplication.translate("StudentDialog", u"Grade 11", None))
        self.class_comboBox.setItemText(12, QCoreApplication.translate("StudentDialog", u"Grade 12", None))

    # retranslateUi

        #Add new pupil
        self.saveStudent_btn.clicked.connect(self.add_student)

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
    
    # Insert new student
    
    def insert_new_student(self):
        
        try:
            connection = self.create_connection()
            if connection is None:
                return
            
            cursor = connection.cursor()

            gender = self.gender_comboBox.currentText()
            student_id = self.generate_pupilId(gender)

            birthday = self.handleDateChange()

            # Assuming birth_date is a QDate object
            birth_date = self.dob_dateEdit.date()

            # Calculate age using the calculate_age method
            age = self.calculate_age(birth_date)
            print(age)

            #First add pupil information
            self.new_pupil = [
                self.name_lineEdit.text(),
                student_id,
                self.gender_comboBox.currentText(),
                self.class_comboBox.currentText(),
                birthday,
                age,
                self.address_lineEdit.text(),
                self.phone_lineEdit.text(),
                self.email_lineEdit.text()
                ]


            #To insert multiplerows in the Sqlite table
            insert_pupil_query = f""" INSERT INTO students_table (names, student_id, gender, class, birthday, age, address, phone_number, email
                                 ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            cursor.execute(insert_pupil_query, self.new_pupil)
            self.show_inserted_message()
            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            # Handle MySQL errors
            print(f"Error: {err}")

    def generate_pupilId(self, gender):

        cursor = self.create_connection().cursor()
        
        while True:
            if gender == "Male":
                id_start_value = "24" + "/U/M"
            else:
                id_start_value = "24" + "/U/F"

            random_value = self.generate_randomNumber()
            student_id = id_start_value + random_value
            
            # Check if the generated student_id already exists in the table
            cursor.execute(f"SELECT student_id FROM students_table WHERE student_id = %s", (student_id,))
            existing_id = cursor.fetchone()
            if not existing_id:
                return student_id

    def generate_randomNumber(self):
        number = randint(1, 1000)
        random_number = f"{number:04d}"
        return random_number
    
    def handleDateChange(self):
        # Convert QDate to a string in the format 'YYYY-MM-DD'
        selected_date = self.dob_dateEdit.date()
        self.date_string = selected_date.toString(Qt.ISODate)

        return self.date_string
    
    def add_student(self):
        self.insert_new_student()
        # Add the logic to save the new pupil data to your data source
        # For now, let's just accept the dialog
        self.accept()

    def show_inserted_message(self):
        # Show a message box with a green tick
        msg_box = QMessageBox(self)
        #msg_box.setIconPixmap(QPixmap('green_tick.png'))  # Replace 'green_tick.png' with the path to your green tick image
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.name_lineEdit.text() + " inserted into the database.")
        msg_box.exec()

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