from PySide6.QtGui import QAction, QIcon
from ui_index import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMenu, QTableWidgetItem, QTableWidget, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QMessageBox, QFileDialog
from ui_index import Ui_MainWindow
import mysql.connector
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

from updateStudentDialog import UpdateStudent

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")

        # Hide dropdowns
        self.icon_text_widget.setHidden(True)
        self.students_dropdown_2.setHidden(True)
        self.teachers_dropdown_2.setHidden(True)
        self.finances_dropdown_2.setHidden(True)

        # Connect buttons to respective context menus
        self.students_btn_1.clicked.connect(self.students_context_menu)
        self.teachers_btn_1.clicked.connect(self.teachers_context_menu)
        self.finances_btn_1.clicked.connect(self.finances_context_menu)

        # Connect buttons to switch to different pages
        self.dashboard_btn_1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard_btn_2.clicked.connect(self.switch_to_dashboardPage)
        self.institution_btn_1.clicked.connect(self.switch_to_institutionPage)
        self.institution_btn_2.clicked.connect(self.switch_to_institutionPage)
        self.student_info_btn_3.clicked.connect(self.switch_to_studentInfoPage)
        self.student_payments_btn_3.clicked.connect(self.switch_to_studentPaymentsPage)
        self.student_transactions_btn_3.clicked.connect(self.switch_to_studentTransactionsPage)
        self.teacher_info_btn_3.clicked.connect(self.switch_to_teacherInfoPage)
        self.teacher_salaries_btn_3.clicked.connect(self.switch_to_teacherSalariesPage)
        self.teacher_transactions_btn_3.clicked.connect(self.switch_to_teacherTransactionsPage)
        self.budgets_btn_3.clicked.connect(self.switch_to_budgetsPage)
        self.expenses_btn_3.clicked.connect(self.switch_to_expensesPage)
        self.business_btn_3.clicked.connect(self.switch_to_businessPage)
        self.settings_btn_2.clicked.connect(self.switch_to_settingsPage)
        self.settings_btn_1.clicked.connect(self.switch_to_settingsPage)

        #Create students tables
        self.create_students_table()

        #Load students table
        self.load_students_generalinfo()
        self.search_student.textChanged.connect(self.search_students)
        self.select_class.currentIndexChanged.connect(self.load_students_generalinfo)
        self.select_gender.currentIndexChanged.connect(self.load_students_generalinfo)

        #Button to open add student dialog
        self.addStudent_btn.clicked.connect(self.open_addStudent_dialog)

        #Excel Export
        self.excelExport_btn.clicked.connect(self.export_to_excel_studentsTable)

        #Pdf Export
        self.pdfExport_btn.clicked.connect(self.export_to_pdf_studentsTable)

        #Control column widths
        #Pupils info table
        self.studentsInfo_table.setColumnWidth(0, 150)
        self.studentsInfo_table.setColumnWidth(1, 80)
        self.studentsInfo_table.setColumnWidth(2, 60)
        self.studentsInfo_table.setColumnWidth(3, 70)
        self.studentsInfo_table.setColumnWidth(4, 70)
        self.studentsInfo_table.setColumnWidth(5, 50)
        self.studentsInfo_table.setColumnWidth(6, 100)
        self.studentsInfo_table.setColumnWidth(7, 80)
        self.studentsInfo_table.setColumnWidth(8, 120)
        self.studentsInfo_table.setColumnWidth(9, 150)

    # Methods to switch to different pages
    def switch_to_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def switch_to_dashboardPage(self):
        self.switch_to_page(0)

    def switch_to_institutionPage(self):
        self.switch_to_page(1)

    def switch_to_studentInfoPage(self):
        self.switch_to_page(2)

    def switch_to_studentPaymentsPage(self):
        self.switch_to_page(3)

    def switch_to_studentTransactionsPage(self):
        self.switch_to_page(4)

    def switch_to_teacherInfoPage(self):
        self.switch_to_page(5)

    def switch_to_teacherSalariesPage(self):
        self.switch_to_page(6)

    def switch_to_teacherTransactionsPage(self):
        self.switch_to_page(7)

    def switch_to_budgetsPage(self):
        self.switch_to_page(8)

    def switch_to_expensesPage(self):
        self.switch_to_page(9)

    def switch_to_businessPage(self):
        self.switch_to_page(10)

    def switch_to_settingsPage(self):
        self.switch_to_page(11)

    # Methods to show context menus
    def students_context_menu(self):
        self.show_custom_context_menu(self.students_btn_1, ["Student Information", "Student Payments", "Student Transactions"])

    def teachers_context_menu(self):
        self.show_custom_context_menu(self.teachers_btn_1, ["Teacher Information", "Teacher Salaries", "Teacher Transactions"])

    def finances_context_menu(self):
        self.show_custom_context_menu(self.finances_btn_1, ["Budgets", "Expenses", "Business Overview"])

    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)

        # Set style for the menu
        menu.setStyleSheet("""
        QMenu {
            background-color: black;
            color: white;
        }

        QMenu::item:selected {
            background-color: white;
            color: #12B298;
        }
        """)

        # Add actions to the menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        # Show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        text = self.sender().text()

        if text == "Student Information":
           self.switch_to_studentInfoPage()
        elif text == "Student Payments":
           self.switch_to_studentPaymentsPage()
        elif text == "Student Transactions":
           self.switch_to_studentPaymentsPage()
        elif text == "Teacher Information":
           self.switch_to_teacherInfoPage()
        elif text == "Teacher Salaries":
           self.switch_to_teacherSalariesPage()
        elif text == "Teacher Transactions":
           self.switch_to_teacherTransactionsPage()
        elif text == "Budgets":
           self.switch_to_budgetsPage()
        elif text == "Expenses":
           self.switch_to_expensesPage()
        elif text == "Business Overview":
           self.switch_to_businessPage()

    # Create Database Connection

    def create_connection(self):
        # Replace these with your actual MySQL server details
        host_name = "localhost"
        user_name = "root"
        mypassword = ""
        database_name = "atepi_school"

        # Establish a connection to MySQL server
        self.mydb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=mypassword
        )

        # Create a cursor to execute SQL queries
        cursor = self.mydb.cursor()

        # Create the database if it doesn't exist
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')

        # Connect to the created database
        self.mydb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=mypassword,
            database=database_name
        )

        return self.mydb

    # Create Pupils Table

    def create_students_table(self):
        # Create a cursor for executing SQL queries
        cursor = self.create_connection().cursor()

        #Pupils table create
        table_name = "students_table"

        create_students_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            names TEXT,
            student_id VARCHAR(15) PRIMARY KEY,
            gender TEXT,
            class TEXT,
            birthday TEXT,
            age INT,
            address TEXT,
            phone_number VARCHAR(15),
            email VARCHAR(15)
        )"""

        cursor.execute(create_students_table_query)

        # Commit changes and close the connection
        self.mydb.commit()
        self.mydb.close

    # Dialog for inserting new student

    def open_addStudent_dialog(self):

        from studentDialog import Ui_StudentDialog
        
        # Instantiate and show the custom dialog
        addStudent_dialog = Ui_StudentDialog(self)
        result = addStudent_dialog.exec() # This will block until the dialog is closed
 
        if result == Ui_StudentDialog.Accepted:
            # If the dialog was accepted (user clicked OK), reload the table data
            self.reload_Studentstable_data()

    def reload_Studentstable_data(self):
        # Clear existing data in the table
        self.studentsInfo_table.setRowCount(0)
        # Rest of your code to repopulate the table...
        self.load_students_generalinfo()

    #LOAD STUDENTS INFORMATION

    def load_students_generalinfo(self):

        # Clear existing data in the table
        self.studentsInfo_table.setRowCount(0)

        # Fetch data based on the selected class and gender
        selected_class = self.select_class.currentText()
        selected_gender = self.select_gender.currentText()
        data = self.get_data_from_table(selected_class, selected_gender)

        # Populate the table with the filtered data
        for row_index, row_data in enumerate(data):
            self.studentsInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.studentsInfo_table.setItem(row_index, col_index, item)

            # Create a custom widget with two buttons lined up horizontally for the second column
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)

            # Set the custom widget as the cell widget for the second column
            self.studentsInfo_table.setCellWidget(row_index, 9, double_button_widget)
            self.studentsInfo_table.setRowHeight(row_index, 50)
        
    def get_data_from_table(self, class_filter, gender_filter):

        table_name = "students_table"
        
        cursor = self.create_connection().cursor()

        # Construct the SQL query based on selected filters
        query = f"""SELECT names, student_id, gender, class, birthday, age, address, phone_number, email 
                    FROM {table_name} 
                    WHERE 
                        ('{class_filter}' = 'SELECT CLASS' OR class = '{class_filter}') AND
                        ('{gender_filter}' = 'SELECT GENDER' OR gender = '{gender_filter}')"""
        
        cursor.execute(query)
        data = cursor.fetchall()
  
        return data
    
    def search_students(self):

        table_name = "students_table" 

        # Clear previous results
        self.studentsInfo_table.setRowCount(0)

        # Get the search query from the QLineEdit
        search_query = self.search_student.text()

        # Execute the SQL query
        cursor = self.create_connection().cursor()
        sql_query = f"""SELECT names, student_id, gender, class, birthday, age, address, phone_number, email FROM {table_name} WHERE names LIKE '%{search_query}%'"""
        cursor.execute(sql_query)
        results = cursor.fetchall()

        # Populate the QTableWidget with the results
        for row_index, row_data in enumerate(results):
            self.studentsInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.studentsInfo_table.setItem(row_index, col_index, item)

        # Create a custom widget with two buttons lined up horizontally for the second column
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)

            # Set the custom widget as the cell widget for the second column
            self.studentsInfo_table.setCellWidget(row_index, 9, double_button_widget)
            self.studentsInfo_table.setRowHeight(row_index, 50)

    
    # EXCEL EXPORT

    def export_to_excel_studentsTable(self):

        # Convert QTableWidget data to pandas DataFrame
        data = []
        self.headers = [self.studentsInfo_table.horizontalHeaderItem(col).text() for col in range(self.studentsInfo_table.columnCount())]
        
        for row in range(self.studentsInfo_table.rowCount()):
        # Check if the item is not None before accessing its text
            row_data = [self.studentsInfo_table.item(row, col).text() if self.studentsInfo_table.item(row, col) is not None else "" for col in range(self.studentsInfo_table.columnCount())]
            data.append(row_data)

        # Create a pandas DataFrame with the collected data and headers
        df = pd.DataFrame(data, columns=self.headers)

        # Save DataFrame to Excel file
        # Exclude the last column before exporting
        df_filtered = df.iloc[:, :-1]

        # Open QFileDialog to get the file path
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save Excel File", "", "Excel Files (*.xlsx);;All Files (*)")

        if file_path:
            # Save filtered DataFrame to Excel file at the chosen path
            df_filtered.to_excel(file_path, index=False)

            print(f"Table exported to {file_path}")

    # PDF EXPORT

    def export_to_pdf_studentsTable(self):

        # Open QFileDialog to get the file path
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save PDF File", "", "PDF Files (*.pdf);;All Files (*)")

        if file_path:
            # Create a PDF document
            pdf_document = SimpleDocTemplate(file_path, pagesize=letter)
            
            # Assuming n is the total number of columns in your QTableWidget
            n = self.studentsInfo_table.columnCount()

            # Extract headers from QTableWidget
            headers = [self.studentsInfo_table.horizontalHeaderItem(col).text() for col in range(n - 1)]

            # Extract data from QTableWidget, excluding the last column
            data = [headers]

            for row in range(self.studentsInfo_table.rowCount()):
                row_data = [self.studentsInfo_table.item(row, col).text() if self.studentsInfo_table.item(row, col) is not None else "" for col in range(n - 1)]
                data.append(row_data)

            # Create a PDF table
            pdf_table = Table(data)

            # Apply styles to the table
            style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1D59F4')),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F4F9FA')),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)])

            pdf_table.setStyle(style)

            # Build the PDF document
            pdf_document.build([pdf_table])

            print(f"Table exported to {file_path}")

    # DOUBLE BUTTON CLASS

class DoubleButtonWidgetStudents(QWidget):
    def __init__(self, row_index, row_data, sidebar):
        super().__init__()

        # Store the row index and row data as instance variables
        self.row_index = row_index
        self.row_data = row_data
        self.sidebar = sidebar  # Store a reference to MySideBar

        #Get pupil variables from tuple
        self.student_name = self.row_data[0]
        self.student_id = self.row_data[1]

        layout = QHBoxLayout(self)

        # Create blue "Edit" button
        self.edit_button = QPushButton("", self)
        self.edit_button.setStyleSheet("background-color: blue; color: white;")
        self.edit_button.setFixedSize(61, 31)
        self.edit_button.clicked.connect(self.edit_clicked)

        # Set an icon for the button
        icon = QIcon(":/Icons/edit.png")  # Replace with the actual path to your icon
        self.edit_button.setIcon(icon)

        # Create red "Delete" button
        self.delete_button = QPushButton("", self)
        self.delete_button.setStyleSheet("background-color: red; color: white; border-radius=10px;")
        self.delete_button.setFixedSize(61, 31)
        self.delete_button.clicked.connect(self.delete_clicked)

        # Set an icon for the button
        icon2 = QIcon(":/Icons/delete.png")  # Replace with the actual path to your icon
        self.delete_button.setIcon(icon2)

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

    def create_connection(self):
        #Create mySQL Database Connection
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = "atepi_school",
            )

        return self.mydb

    def edit_clicked(self):
        # Create an instance of UpdateStudent dialog
        self.update_dialog = UpdateStudent(self.row_index, self.row_data)
        
        # Connect the custom signal to reload_Studentstable_data slot in MySideBar
        self.update_dialog.data_updated.connect(self.sidebar.reload_Studentstable_data)
        
        # Execute the dialog
        self.update_dialog.exec()

    def delete_clicked(self):

        cursor = self.create_connection().cursor()

        # Create a confirmation dialog
        message = QMessageBox.question(
            self, 'Confirmation',
            'Are you sure that you want to delete ' + self.student_name + '?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
    
        if message == QMessageBox.StandardButton.Yes:
            # Delete the row from the database
            cursor = self.create_connection().cursor()
            sql_query = "DELETE FROM students_table WHERE student_id=%s"
            cursor.execute(sql_query, (self.student_id,))
            self.mydb.commit()
            self.mydb.close()

            # Emit a signal to inform about data change
            self.sidebar.reload_Studentstable_data()


  

