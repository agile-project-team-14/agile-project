# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buildingAdmin_Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Employees_Managment2new as EM2
from buildingAdmin import viewReservationsBAN as VR
from login import gui as G

def close():
    buildingAdmin_Dashboard.close()
    pass

class Ui_buildingAdmin_Dashboard(object):

    def logOut(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = G.Ui_LoginWindow()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        close()

    def back(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = G.Ui_LoginWindow()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        close()

    def showReservations2(self):
        self.viewReservations = QtWidgets.QMainWindow()
        self.ui = VR.Ui_viewReservations()
        self.ui.setupUi(self.viewReservations)
        self.viewReservations.show()
        close()

    def showEmployessManagment2(self):
        self.Employees_Managment = QtWidgets.QMainWindow()
        self.ui = EM2.Ui_Employees_Managment()
        self.ui.setupUi(self.Employees_Managment)
        self.Employees_Managment.show()
        close()

    def setupUi(self, buildingAdmin_Dashboard):
        buildingAdmin_Dashboard.setObjectName("buildingAdmin_Dashboard")
        buildingAdmin_Dashboard.resize(1200, 600)
        buildingAdmin_Dashboard.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(buildingAdmin_Dashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(20, 30, 71, 61))
        self.logoLabel.setStyleSheet("background-image: url(imageedit_2_5347177992.jpg);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.logOut())
        self.logOutButton.setGeometry(QtCore.QRect(1090, 30, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.logOutButton.setFont(font)
        self.logOutButton.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"image: url(logout (2).png);\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"border-radius:6px;\n"
"padding: 10px; \n"
"")
        self.logOutButton.setText("")
        self.logOutButton.setObjectName("logOutButton")
        self.employeeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showEmployessManagment2())
        self.employeeButton.setGeometry(QtCore.QRect(160, 430, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.employeeButton.setFont(font)
        self.employeeButton.setStyleSheet("QPushButton {\n"
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
        self.employeeButton.setObjectName("employeeButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.back())
        self.backButton.setGeometry(QtCore.QRect(970, 30, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"image: url(left-arrow-in-circular-button.png);\n"
"color: rgb(255, 255, 255);\n"
"text-align: center;\n"
"border-radius:6px;\n"
"padding: 10px; \n"
"")
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        self.adminDashboardLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_3.setGeometry(QtCore.QRect(45, 140, 921, 71))
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
        self.reservationsButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showReservations2())
        self.reservationsButton.setGeometry(QtCore.QRect(750, 430, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.reservationsButton.setFont(font)
        self.reservationsButton.setStyleSheet("QPushButton {\n"
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
        self.reservationsButton.setObjectName("reservationsButton")
        self.adminDashboardLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_2.setGeometry(QtCore.QRect(420, 240, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.adminDashboardLabel_2.setFont(font)
        self.adminDashboardLabel_2.setStyleSheet("color: rgb(41, 84, 125);\n"
"text-align: left;\n"
"")
        self.adminDashboardLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.adminDashboardLabel_2.setObjectName("adminDashboardLabel_2")
        buildingAdmin_Dashboard.setCentralWidget(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1181, 581))
        self.label.setStyleSheet("background-image: url(background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.lower()


        self.statusbar = QtWidgets.QStatusBar(buildingAdmin_Dashboard)
        self.statusbar.setObjectName("statusbar")
        buildingAdmin_Dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(buildingAdmin_Dashboard)
        QtCore.QMetaObject.connectSlotsByName(buildingAdmin_Dashboard)

    def retranslateUi(self, buildingAdmin_Dashboard):
        _translate = QtCore.QCoreApplication.translate
        buildingAdmin_Dashboard.setWindowTitle(_translate("buildingAdmin_Dashboard", "Building Admin Dashboard"))
        self.employeeButton.setText(_translate("buildingAdmin_Dashboard", "Employee"))
        self.adminDashboardLabel_3.setText(_translate("buildingAdmin_Dashboard", "Building Admin Dashboard"))
        self.reservationsButton.setText(_translate("buildingAdmin_Dashboard", "Reservations"))
        self.adminDashboardLabel_2.setText(_translate("buildingAdmin_Dashboard", "Mangament"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    buildingAdmin_Dashboard = QtWidgets.QMainWindow()
    ui = Ui_buildingAdmin_Dashboard()
    ui.setupUi(buildingAdmin_Dashboard)
    buildingAdmin_Dashboard.show()
    sys.exit(app.exec_())