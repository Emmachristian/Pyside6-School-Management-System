from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 867)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1231, 871))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.layoutWidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border:none;\n"
"	border-radius: 3px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.label_6 = QLabel(self.icon_only_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/Icons/logo.png"))
        self.label_6.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 40, -1, -1)
        self.dashboard_btn_1 = QPushButton(self.icon_only_widget)
        self.dashboard_btn_1.setObjectName(u"dashboard_btn_1")
        self.dashboard_btn_1.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/dashboardsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/Icons/dashboardsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_btn_1.setIcon(icon)
        self.dashboard_btn_1.setIconSize(QSize(18, 18))
        self.dashboard_btn_1.setCheckable(True)
        self.dashboard_btn_1.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.dashboard_btn_1)

        self.institution_btn_1 = QPushButton(self.icon_only_widget)
        self.institution_btn_1.setObjectName(u"institution_btn_1")
        self.institution_btn_1.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/institutionsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/Icons/institutionsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.institution_btn_1.setIcon(icon1)
        self.institution_btn_1.setIconSize(QSize(23, 23))
        self.institution_btn_1.setCheckable(True)
        self.institution_btn_1.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.institution_btn_1)

        self.students_btn_1 = QPushButton(self.icon_only_widget)
        self.students_btn_1.setObjectName(u"students_btn_1")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/studentssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/Icons/studentssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.students_btn_1.setIcon(icon2)
        self.students_btn_1.setIconSize(QSize(20, 20))
        self.students_btn_1.setCheckable(True)
        self.students_btn_1.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.students_btn_1)

        self.teachers_btn_1 = QPushButton(self.icon_only_widget)
        self.teachers_btn_1.setObjectName(u"teachers_btn_1")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/teacherssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/Icons/teacherssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.teachers_btn_1.setIcon(icon3)
        self.teachers_btn_1.setIconSize(QSize(20, 20))
        self.teachers_btn_1.setCheckable(True)
        self.teachers_btn_1.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.teachers_btn_1)

        self.finances_btn_1 = QPushButton(self.icon_only_widget)
        self.finances_btn_1.setObjectName(u"finances_btn_1")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/financessmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/Icons/financessmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.finances_btn_1.setIcon(icon4)
        self.finances_btn_1.setIconSize(QSize(20, 20))
        self.finances_btn_1.setCheckable(True)
        self.finances_btn_1.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.finances_btn_1)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 419, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settings_btn_1 = QPushButton(self.icon_only_widget)
        self.settings_btn_1.setObjectName(u"settings_btn_1")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/settingssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/Icons/settingssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_btn_1.setIcon(icon5)
        self.settings_btn_1.setIconSize(QSize(20, 20))
        self.settings_btn_1.setCheckable(True)
        self.settings_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.settings_btn_1)

        self.signout_btn_1 = QPushButton(self.icon_only_widget)
        self.signout_btn_1.setObjectName(u"signout_btn_1")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/signoutsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/Icons/signoutsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.signout_btn_1.setIcon(icon6)
        self.signout_btn_1.setIconSize(QSize(20, 20))
        self.signout_btn_1.setCheckable(True)
        self.signout_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.signout_btn_1)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.layoutWidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton { \n"
"	height: 30px;\n"
"    border:none;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, -1, 0, -1)
        self.label_4 = QLabel(self.icon_text_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/Icons/logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.icon_text_widget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_btn_2 = QPushButton(self.icon_text_widget)
        self.dashboard_btn_2.setObjectName(u"dashboard_btn_2")
        self.dashboard_btn_2.setStyleSheet(u"QPushButton { \n"
"	padding-left:-60px;\n"
"	height: 30px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border:none;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/dashboard2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/Icons/dashboard1.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_btn_2.setIcon(icon7)
        self.dashboard_btn_2.setIconSize(QSize(100, 60))
        self.dashboard_btn_2.setCheckable(True)
        self.dashboard_btn_2.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.dashboard_btn_2)

        self.institution_btn_2 = QPushButton(self.icon_text_widget)
        self.institution_btn_2.setObjectName(u"institution_btn_2")
        self.institution_btn_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-65px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border:none;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/institution2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/Icons/institution1.png", QSize(), QIcon.Normal, QIcon.On)
        self.institution_btn_2.setIcon(icon8)
        self.institution_btn_2.setIconSize(QSize(100, 60))
        self.institution_btn_2.setCheckable(True)
        self.institution_btn_2.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.institution_btn_2)

        self.frame = QFrame(self.icon_text_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.students_btn_3 = QPushButton(self.frame)
        self.students_btn_3.setObjectName(u"students_btn_3")
        self.students_btn_3.setStyleSheet(u"height:30px;")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/students3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/Icons/students4.png", QSize(), QIcon.Normal, QIcon.On)
        self.students_btn_3.setIcon(icon9)
        self.students_btn_3.setIconSize(QSize(200, 60))
        self.students_btn_3.setCheckable(True)
        self.students_btn_3.setAutoExclusive(False)

        self.verticalLayout_7.addWidget(self.students_btn_3)

        self.students_dropdown_2 = QFrame(self.frame)
        self.students_dropdown_2.setObjectName(u"students_dropdown_2")
        self.students_dropdown_2.setStyleSheet(u"background-color: rgb(29, 38, 27);")
        self.students_dropdown_2.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.students_dropdown_2)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.student_info_btn_3 = QPushButton(self.students_dropdown_2)
        self.student_info_btn_3.setObjectName(u"student_info_btn_3")
        self.student_info_btn_3.setStyleSheet(u"QPushButton {\n"
"  padding-left: 20px;\n"
"  height: 30px;\n"
"  border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #12B298;\n"
"}")
        self.student_info_btn_3.setCheckable(True)
        self.student_info_btn_3.setAutoExclusive(False)

        self.verticalLayout_23.addWidget(self.student_info_btn_3)

        self.student_payments_btn_3 = QPushButton(self.students_dropdown_2)
        self.student_payments_btn_3.setObjectName(u"student_payments_btn_3")
        self.student_payments_btn_3.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"padding-left: 11px;\n"
"height: 30px;\n"
" border:none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: #12B298;\n"
"}")
        self.student_payments_btn_3.setCheckable(True)
        self.student_payments_btn_3.setAutoExclusive(False)

        self.verticalLayout_23.addWidget(self.student_payments_btn_3)

        self.student_transactions_btn_3 = QPushButton(self.students_dropdown_2)
        self.student_transactions_btn_3.setObjectName(u"student_transactions_btn_3")
        self.student_transactions_btn_3.setStyleSheet(u"QPushButton {\n"
"padding-left: 25px;\n"
"height: 30px;\n"
" border:none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: #12B298;\n"
"}")
        self.student_transactions_btn_3.setCheckable(True)
        self.student_transactions_btn_3.setAutoExclusive(False)

        self.verticalLayout_23.addWidget(self.student_transactions_btn_3)


        self.verticalLayout_7.addWidget(self.students_dropdown_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.icon_text_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.teachers_btn_4 = QPushButton(self.frame_2)
        self.teachers_btn_4.setObjectName(u"teachers_btn_4")
        self.teachers_btn_4.setStyleSheet(u"height: 30px;")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/teachers3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/Icons/teachers4.png", QSize(), QIcon.Normal, QIcon.On)
        self.teachers_btn_4.setIcon(icon10)
        self.teachers_btn_4.setIconSize(QSize(200, 60))
        self.teachers_btn_4.setCheckable(True)
        self.teachers_btn_4.setAutoExclusive(False)

        self.verticalLayout_8.addWidget(self.teachers_btn_4)

        self.teachers_dropdown_2 = QFrame(self.frame_2)
        self.teachers_dropdown_2.setObjectName(u"teachers_dropdown_2")
        self.teachers_dropdown_2.setEnabled(True)
        self.teachers_dropdown_2.setStyleSheet(u"background-color: rgb(29, 38, 27);")
        self.teachers_dropdown_2.setFrameShape(QFrame.StyledPanel)
        self.teachers_dropdown_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.teachers_dropdown_2)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.teacher_info_btn_3 = QPushButton(self.teachers_dropdown_2)
        self.teacher_info_btn_3.setObjectName(u"teacher_info_btn_3")
        self.teacher_info_btn_3.setStyleSheet(u"QPushButton {\n"
"padding-left: 20px;\n"
"height: 30px;\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    color: #12B298;\n"
"}")
        self.teacher_info_btn_3.setCheckable(True)
        self.teacher_info_btn_3.setAutoExclusive(False)

        self.verticalLayout_24.addWidget(self.teacher_info_btn_3)

        self.teacher_salaries_btn_3 = QPushButton(self.teachers_dropdown_2)
        self.teacher_salaries_btn_3.setObjectName(u"teacher_salaries_btn_3")
        self.teacher_salaries_btn_3.setStyleSheet(u"QPushButton {\n"
"padding-left: 4px;\n"
"height: 30px;\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    color: #12B298;\n"
"}")
        self.teacher_salaries_btn_3.setCheckable(True)
        self.teacher_salaries_btn_3.setAutoExclusive(False)

        self.verticalLayout_24.addWidget(self.teacher_salaries_btn_3)

        self.teacher_transactions_btn_3 = QPushButton(self.teachers_dropdown_2)
        self.teacher_transactions_btn_3.setObjectName(u"teacher_transactions_btn_3")
        self.teacher_transactions_btn_3.setStyleSheet(u"QPushButton {\n"
"padding-left: 25px;\n"
"height: 30px;\n"
"border:none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: #12B298;\n"
"}")
        self.teacher_transactions_btn_3.setCheckable(True)
        self.teacher_transactions_btn_3.setAutoExclusive(False)

        self.verticalLayout_24.addWidget(self.teacher_transactions_btn_3)


        self.verticalLayout_8.addWidget(self.teachers_dropdown_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.icon_text_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.finances_btn_3 = QPushButton(self.frame_3)
        self.finances_btn_3.setObjectName(u"finances_btn_3")
        self.finances_btn_3.setStyleSheet(u"height: 30px;")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/finances3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/Icons/finances4.png", QSize(), QIcon.Normal, QIcon.On)
        self.finances_btn_3.setIcon(icon11)
        self.finances_btn_3.setIconSize(QSize(200, 60))
        self.finances_btn_3.setCheckable(True)
        self.finances_btn_3.setAutoExclusive(False)

        self.verticalLayout_9.addWidget(self.finances_btn_3)

        self.finances_dropdown_2 = QFrame(self.frame_3)
        self.finances_dropdown_2.setObjectName(u"finances_dropdown_2")
        self.finances_dropdown_2.setStyleSheet(u"background-color: rgb(29, 38, 27);")
        self.finances_dropdown_2.setFrameShape(QFrame.StyledPanel)
        self.finances_dropdown_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.finances_dropdown_2)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.budgets_btn_3 = QPushButton(self.finances_dropdown_2)
        self.budgets_btn_3.setObjectName(u"budgets_btn_3")
        self.budgets_btn_3.setStyleSheet(u"QPushButton {\n"
"padding-left: -40px;\n"
"height: 30px;\n"
"border:none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: #12B298;\n"
"}")
        self.budgets_btn_3.setCheckable(True)
        self.budgets_btn_3.setAutoExclusive(False)

        self.verticalLayout_25.addWidget(self.budgets_btn_3)

        self.expenses_btn_3 = QPushButton(self.finances_dropdown_2)
        self.expenses_btn_3.setObjectName(u"expenses_btn_3")
        self.expenses_btn_3.setStyleSheet(u"QPushButton {\n"
"padding-left: -32px;\n"
"height: 30px;\n"
"border:none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: #12B298;\n"
"}")
        self.expenses_btn_3.setCheckable(True)
        self.expenses_btn_3.setAutoExclusive(False)

        self.verticalLayout_25.addWidget(self.expenses_btn_3)

        self.business_btn_3 = QPushButton(self.finances_dropdown_2)
        self.business_btn_3.setObjectName(u"business_btn_3")
        self.business_btn_3.setStyleSheet(u"QPushButton {\n"
"padding-left: 13px;\n"
"height: 30px;\n"
"border:none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: #12B298;\n"
"}")
        self.business_btn_3.setCheckable(True)
        self.business_btn_3.setAutoExclusive(False)

        self.verticalLayout_25.addWidget(self.business_btn_3)


        self.verticalLayout_9.addWidget(self.finances_dropdown_2)


        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 135, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.settings_btn_2 = QPushButton(self.icon_text_widget)
        self.settings_btn_2.setObjectName(u"settings_btn_2")
        self.settings_btn_2.setStyleSheet(u"QPushButton { \n"
"	padding-left:-65px;\n"
"	height: 30px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border:none;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/Icons/settings2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/Icons/settings1.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_btn_2.setIcon(icon12)
        self.settings_btn_2.setIconSize(QSize(100, 60))
        self.settings_btn_2.setCheckable(True)
        self.settings_btn_2.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.settings_btn_2)

        self.signout_btn_2 = QPushButton(self.icon_text_widget)
        self.signout_btn_2.setObjectName(u"signout_btn_2")
        self.signout_btn_2.setStyleSheet(u"QPushButton { \n"
"	padding-left:-58px;\n"
"	height: 30px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border:none;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/Icons/signout2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/Icons/signout1.png", QSize(), QIcon.Normal, QIcon.On)
        self.signout_btn_2.setIcon(icon13)
        self.signout_btn_2.setIconSize(QSize(100, 16))
        self.signout_btn_2.setCheckable(True)
        self.signout_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.signout_btn_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.pushButton_4 = QPushButton(self.header_widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/Icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon14)
        self.pushButton_4.setIconSize(QSize(25, 35))
        self.pushButton_4.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(20, -1, -1, -1)
        self.label_7 = QLabel(self.header_widget)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_7.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_7)

        self.label_8 = QLabel(self.header_widget)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(79, 79, 79);")

        self.verticalLayout_16.addWidget(self.label_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_16)

        self.horizontalSpacer = QSpacerItem(356, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 30))
        self.lineEdit.setMaximumSize(QSize(300, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label_9 = QLabel(self.header_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(40, 40))
        self.label_9.setMaximumSize(QSize(40, 40))
        self.label_9.setPixmap(QPixmap(u":/Icons/profile.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_9)


        self.verticalLayout_13.addWidget(self.header_widget)

        self.body_widget = QWidget(self.layoutWidget)
        self.body_widget.setObjectName(u"body_widget")
        self.body_widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.body_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.body_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.label_2 = QLabel(self.dashboard_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 270, 361, 91))
        font3 = QFont()
        font3.setPointSize(50)
        self.label_2.setFont(font3)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.institution_page = QWidget()
        self.institution_page.setObjectName(u"institution_page")
        self.label_10 = QLabel(self.institution_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(310, 280, 361, 91))
        self.label_10.setFont(font3)
        self.stackedWidget.addWidget(self.institution_page)
        self.student_info_page = QWidget()
        self.student_info_page.setObjectName(u"student_info_page")
        self.label_11 = QLabel(self.student_info_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 10, 191, 31))
        font4 = QFont()
        font4.setFamilies([u"Poppins SemiBold"])
        font4.setPointSize(20)
        self.label_11.setFont(font4)
        self.label_21 = QLabel(self.student_info_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 40, 361, 21))
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setPointSize(10)
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"color: rgb(81, 81, 81);")
        self.studentsInfo_table = QTableWidget(self.student_info_page)
        if (self.studentsInfo_table.columnCount() < 10):
            self.studentsInfo_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.studentsInfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.studentsInfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.studentsInfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.studentsInfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.studentsInfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.studentsInfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.studentsInfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.studentsInfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.studentsInfo_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.studentsInfo_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.studentsInfo_table.setObjectName(u"studentsInfo_table")
        self.studentsInfo_table.setGeometry(QRect(20, 190, 950, 591))
        self.studentsInfo_table.setMinimumSize(QSize(0, 591))
        self.studentsInfo_table.setMaximumSize(QSize(16777215, 591))
        self.studentsInfo_table.setStyleSheet(u"QHeaderView::section {\n"
"                font-weight: bold;\n"
"				background-color:black;\n"
"				color:white;\n"
"            }\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}\n"
"")
        self.studentsInfo_table.setAlternatingRowColors(True)
        self.widget = QWidget(self.student_info_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 461, 43))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.addStudent_btn = QPushButton(self.widget)
        self.addStudent_btn.setObjectName(u"addStudent_btn")
        self.addStudent_btn.setMinimumSize(QSize(141, 41))
        self.addStudent_btn.setStyleSheet(u"background-color:#000000;\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12px;")
        icon15 = QIcon()
        icon15.addFile(u":/Icons/add student.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addStudent_btn.setIcon(icon15)

        self.horizontalLayout_4.addWidget(self.addStudent_btn)

        self.excelExport_btn = QPushButton(self.widget)
        self.excelExport_btn.setObjectName(u"excelExport_btn")
        self.excelExport_btn.setMinimumSize(QSize(151, 41))
        self.excelExport_btn.setStyleSheet(u"background-color:#00E159;\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12px;")
        icon16 = QIcon()
        icon16.addFile(u":/Icons/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.excelExport_btn.setIcon(icon16)

        self.horizontalLayout_4.addWidget(self.excelExport_btn)

        self.pdfExport_btn = QPushButton(self.widget)
        self.pdfExport_btn.setObjectName(u"pdfExport_btn")
        self.pdfExport_btn.setMinimumSize(QSize(151, 41))
        self.pdfExport_btn.setStyleSheet(u"background-color: rgb(255, 60, 60);\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12px;")
        icon17 = QIcon()
        icon17.addFile(u":/Icons/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pdfExport_btn.setIcon(icon17)

        self.horizontalLayout_4.addWidget(self.pdfExport_btn)

        self.widget1 = QWidget(self.student_info_page)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 130, 771, 43))
        self.horizontalLayout_5 = QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.select_gender = QComboBox(self.widget1)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(0, 41))
        self.select_gender.setStyleSheet(u" QComboBox {\n"
"                border: 2px solid #ffffff;\n"
"                border-radius: 8px;\n"
"                padding: 1px 18px 1px 3px;\n"
"                background: black;\n"
"                selection-background-color: #2980b9;\n"
"				padding-left:15px;\n"
"                color: white;\n"
"				font-weight:bold;\n"
"            }")

        self.horizontalLayout_5.addWidget(self.select_gender)

        self.select_class = QComboBox(self.widget1)
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.setObjectName(u"select_class")
        self.select_class.setMinimumSize(QSize(0, 41))
        self.select_class.setStyleSheet(u" QComboBox {\n"
"                border: 2px solid #ffffff;\n"
"                border-radius: 8px;\n"
"                padding: 1px 18px 1px 3px;\n"
"                background: black;\n"
"                selection-background-color: #2980b9;\n"
"				padding-left:15px;\n"
"                color: white;\n"
"				font-weight:bold;\n"
"            }")

        self.horizontalLayout_5.addWidget(self.select_class)

        self.search_student = QLineEdit(self.widget1)
        self.search_student.setObjectName(u"search_student")
        self.search_student.setMinimumSize(QSize(300, 38))
        self.search_student.setMaximumSize(QSize(300, 38))
        self.search_student.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.search_student)

        self.stackedWidget.addWidget(self.student_info_page)
        self.student_payments_page = QWidget()
        self.student_payments_page.setObjectName(u"student_payments_page")
        self.label_12 = QLabel(self.student_payments_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(250, 290, 551, 91))
        self.label_12.setFont(font3)
        self.stackedWidget.addWidget(self.student_payments_page)
        self.student_transactions_page = QWidget()
        self.student_transactions_page.setObjectName(u"student_transactions_page")
        self.label_13 = QLabel(self.student_transactions_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(200, 280, 631, 91))
        self.label_13.setFont(font3)
        self.stackedWidget.addWidget(self.student_transactions_page)
        self.teacher_info_page = QWidget()
        self.teacher_info_page.setObjectName(u"teacher_info_page")
        self.label_14 = QLabel(self.teacher_info_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(280, 280, 421, 91))
        self.label_14.setFont(font3)
        self.stackedWidget.addWidget(self.teacher_info_page)
        self.teacher_salaries_page = QWidget()
        self.teacher_salaries_page.setObjectName(u"teacher_salaries_page")
        self.label_15 = QLabel(self.teacher_salaries_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(260, 290, 511, 91))
        self.label_15.setFont(font3)
        self.stackedWidget.addWidget(self.teacher_salaries_page)
        self.teacher_transactions_page = QWidget()
        self.teacher_transactions_page.setObjectName(u"teacher_transactions_page")
        self.label_20 = QLabel(self.teacher_transactions_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(170, 310, 641, 91))
        self.label_20.setFont(font3)
        self.stackedWidget.addWidget(self.teacher_transactions_page)
        self.budgets_page = QWidget()
        self.budgets_page.setObjectName(u"budgets_page")
        self.label_16 = QLabel(self.budgets_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(350, 290, 291, 91))
        self.label_16.setFont(font3)
        self.stackedWidget.addWidget(self.budgets_page)
        self.expenses_page = QWidget()
        self.expenses_page.setObjectName(u"expenses_page")
        self.label_17 = QLabel(self.expenses_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(360, 300, 291, 91))
        self.label_17.setFont(font3)
        self.stackedWidget.addWidget(self.expenses_page)
        self.business_page = QWidget()
        self.business_page.setObjectName(u"business_page")
        self.label_18 = QLabel(self.business_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(250, 290, 551, 91))
        self.label_18.setFont(font3)
        self.stackedWidget.addWidget(self.business_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_19 = QLabel(self.settings_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(380, 290, 271, 91))
        self.label_19.setFont(font3)
        self.stackedWidget.addWidget(self.settings_page)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_13.addWidget(self.body_widget)


        self.gridLayout.addLayout(self.verticalLayout_13, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_4.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton_4.toggled.connect(self.icon_only_widget.setVisible)
        self.dashboard_btn_2.toggled.connect(self.dashboard_btn_1.setChecked)
        self.institution_btn_2.toggled.connect(self.institution_btn_1.setChecked)
        self.settings_btn_2.toggled.connect(self.settings_btn_1.setChecked)
        self.signout_btn_2.toggled.connect(self.signout_btn_1.setChecked)
        self.signout_btn_1.toggled.connect(MainWindow.close)
        self.signout_btn_2.toggled.connect(MainWindow.close)
        self.finances_btn_3.toggled.connect(self.finances_dropdown_2.setHidden)
        self.students_btn_3.toggled.connect(self.students_dropdown_2.setHidden)
        self.teachers_btn_4.toggled.connect(self.teachers_dropdown_2.setHidden)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText("")
        self.dashboard_btn_1.setText("")
        self.institution_btn_1.setText("")
        self.students_btn_1.setText("")
        self.teachers_btn_1.setText("")
        self.finances_btn_1.setText("")
        self.settings_btn_1.setText("")
        self.signout_btn_1.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"School", None))
        self.dashboard_btn_2.setText("")
        self.institution_btn_2.setText("")
        self.students_btn_3.setText("")
        self.student_info_btn_3.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.student_payments_btn_3.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.student_transactions_btn_3.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.teachers_btn_4.setText("")
        self.teacher_info_btn_3.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.teacher_salaries_btn_3.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.teacher_transactions_btn_3.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.finances_btn_3.setText("")
        self.budgets_btn_3.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.expenses_btn_3.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.business_btn_3.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.settings_btn_2.setText("")
        self.signout_btn_2.setText("")
        self.pushButton_4.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hello, Mark", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Welcome to your page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search here...", None))
        self.label_9.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Institution", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Student Info", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Welcome to the students information page", None))
        ___qtablewidgetitem = self.studentsInfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.studentsInfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Student ID", None));
        ___qtablewidgetitem2 = self.studentsInfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem3 = self.studentsInfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem4 = self.studentsInfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Birthday", None));
        ___qtablewidgetitem5 = self.studentsInfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem6 = self.studentsInfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem7 = self.studentsInfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem8 = self.studentsInfo_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem9 = self.studentsInfo_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.addStudent_btn.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.excelExport_btn.setText(QCoreApplication.translate("MainWindow", u"Excel Export", None))
        self.pdfExport_btn.setText(QCoreApplication.translate("MainWindow", u"Pdf Export", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT GENDER", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.select_class.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT CLASS", None))
        self.select_class.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.select_class.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.select_class.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.select_class.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.select_class.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.select_class.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.select_class.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.select_class.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.select_class.setItemText(9, QCoreApplication.translate("MainWindow", u"Grade 9", None))
        self.select_class.setItemText(10, QCoreApplication.translate("MainWindow", u"Grade 10", None))
        self.select_class.setItemText(11, QCoreApplication.translate("MainWindow", u"Grade 11", None))
        self.select_class.setItemText(12, QCoreApplication.translate("MainWindow", u"Grade 12", None))

        self.search_student.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Student...", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Teacher Info", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

