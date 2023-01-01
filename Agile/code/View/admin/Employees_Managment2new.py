# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Employees_Managment2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import addNewEmployeesnew as addE2
import modifyEmployeenew as mE2
import deleteEmployeenew as DE2
from login import gui as G
import buildingAdmin_Dashboardnew as BM

# close function
def close():
    Employees_Managment.close()
    pass

class Ui_Employees_Managment(object):'
    # logout function
    def logOut(self):
                self.LoginWindow = QtWidgets.QMainWindow()
                self.ui = G.Ui_LoginWindow()
                self.ui.setupUi(self.LoginWindow)
                self.LoginWindow.show()
                close()
    # back function
    def back(self):
                self.buildingAdmin_Dashboard = QtWidgets.QMainWindow()
                self.ui = BM.Ui_buildingAdmin_Dashboard()
                self.ui.setupUi(self.buildingAdmin_Dashboard)
                self.buildingAdmin_Dashboard.show()
                close()

     # transitions Functions
    def showAddNewEmployees2(self):
        self.addNewEmployee = QtWidgets.QMainWindow()
        self.ui = addE2.Ui_addNewEmployee()
        self.ui.setupUi(self.addNewEmployee)
        self.addNewEmployee.show()
        close()

    def showModifyEmployees2(self):
        self.modifyEmployee = QtWidgets.QMainWindow()
        self.ui = mE2.Ui_modifyEmployee()
        self.ui.setupUi(self.modifyEmployee)
        self.modifyEmployee.show()
        close()


    def showaDeleteEmployees2(self):
        self.deleteEmployee = QtWidgets.QMainWindow()
        self.ui = DE2.Ui_deleteEmployee()
        self.ui.setupUi(self.deleteEmployee)
        self.deleteEmployee.show()
        close()

    # UI setUp function
    def setupUi(self, Employees_Managment):
        Employees_Managment.setObjectName("Employees_Managment")
        Employees_Managment.resize(1200, 600)
        Employees_Managment.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(Employees_Managment)
        self.centralwidget.setObjectName("centralwidget")
        self.adminDashboardLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_2.setGeometry(QtCore.QRect(270, 240, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.adminDashboardLabel_2.setFont(font)
        self.adminDashboardLabel_2.setStyleSheet("color: rgb(41, 84, 125);\n"
"text-align: left;\n"
"")
        self.adminDashboardLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.adminDashboardLabel_2.setObjectName("adminDashboardLabel_2")
        self.adminDashboardLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_3.setGeometry(QtCore.QRect(50, 140, 921, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.adminDashboardLabel_3.setFont(font)
        self.adminDashboardLabel_3.setStyleSheet("color: rgb(170, 0, 0);\n"
"text-align: left;\n"
"")
        self.adminDashboardLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.adminDashboardLabel_3.setObjectName("adminDashboardLabel_3")
        self.showResidentInfoPushButton_2 = QtWidgets.QPushButton(self.centralwidget,  clicked=lambda: self.logOut())
        self.showResidentInfoPushButton_2.setGeometry(QtCore.QRect(1090, 30, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.showResidentInfoPushButton_2.setFont(font)
        self.showResidentInfoPushButton_2.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"image: url(logout (2).png);\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"border-radius:6px;\n"
"padding: 10px; \n"
"")
        self.showResidentInfoPushButton_2.setText("")
        self.showResidentInfoPushButton_2.setObjectName("showResidentInfoPushButton_2")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showAddNewEmployees2())
        self.addButton.setGeometry(QtCore.QRect(60, 430, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("QPushButton {\n"
                                     "background-color: rgb(0,100,150);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "QPushButton:hover\n"
                                     "{\n"
                                     "background-color: rgb(170,0,0);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}"
)
        self.addButton.setObjectName("addButton")
        self.modifyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showModifyEmployees2())
        self.modifyButton.setGeometry(QtCore.QRect(450, 430, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.modifyButton.setFont(font)
        self.modifyButton.setStyleSheet("QPushButton {\n"
                                     "background-color: rgb(0,100,150);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "QPushButton:hover\n"
                                     "{\n"
                                     "background-color: rgb(170,0,0);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}"
)
        self.modifyButton.setObjectName("modifyButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showaDeleteEmployees2())
        self.deleteButton.setGeometry(QtCore.QRect(830, 430, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("QPushButton {\n"
                                     "background-color: rgb(0,100,150);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "QPushButton:hover\n"
                                     "{\n"
                                     "background-color: rgb(170,0,0);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}"
)
        self.deleteButton.setObjectName("deleteButton")
        self.idLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_2.setGeometry(QtCore.QRect(800, 230, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_2.setFont(font)
        self.idLabel_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(businessman (1).png);")
        self.idLabel_2.setText("")
        self.idLabel_2.setObjectName("idLabel_2")
        self.showResidentInfoPushButton_3 = QtWidgets.QPushButton(self.centralwidget,  clicked=lambda: self.back())
        self.showResidentInfoPushButton_3.setGeometry(QtCore.QRect(970, 30, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.showResidentInfoPushButton_3.setFont(font)
        self.showResidentInfoPushButton_3.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"image: url(left-arrow-in-circular-button.png);\n"
"color: rgb(255, 255, 255);\n"
"text-align: center;\n"
"border-radius:6px;\n"
"padding: 10px; \n"
"")
        self.showResidentInfoPushButton_3.setText("")
        self.showResidentInfoPushButton_3.setObjectName("showResidentInfoPushButton_3")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(20, 30, 71, 61))
        self.logoLabel.setStyleSheet("background-image: url(imageedit_2_5347177992.jpg);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        Employees_Managment.setCentralWidget(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1181, 581))
        self.label.setStyleSheet("background-image: url(background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.lower()

        self.statusbar = QtWidgets.QStatusBar(Employees_Managment)
        self.statusbar.setObjectName("statusbar")
        Employees_Managment.setStatusBar(self.statusbar)

        self.retranslateUi(Employees_Managment)
        QtCore.QMetaObject.connectSlotsByName(Employees_Managment)

    def retranslateUi(self, Employees_Managment):
        _translate = QtCore.QCoreApplication.translate
        Employees_Managment.setWindowTitle(_translate("Employees_Managment", "EmployeesManagment"))
        self.adminDashboardLabel_2.setText(_translate("Employees_Managment", "Employee Managment"))
        self.adminDashboardLabel_3.setText(_translate("Employees_Managment", "Building Admin Dashboard"))
        self.addButton.setText(_translate("Employees_Managment", "Add"))
        self.modifyButton.setText(_translate("Employees_Managment", "Modify"))
        self.deleteButton.setText(_translate("Employees_Managment", "Delete"))


# main
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Employees_Managment = QtWidgets.QMainWindow()
    ui = Ui_Employees_Managment()
    ui.setupUi(Employees_Managment)
    Employees_Managment.show()
    sys.exit(app.exec_())
