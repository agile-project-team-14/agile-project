# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reservations_Managment.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Admin_Dashboardnew as AD
from login import gui as G
from admin import viewReservationsAN as VR
import deleteReservationsAN as DR

def close():
    Reservations_Managment.close()
    pass

class Ui_Reservations_Managment(object):

    def showReservations2(self):
        self.viewReservations = QtWidgets.QMainWindow()
        self.ui = VR.Ui_viewReservations()
        self.ui.setupUi(self.viewReservations)
        self.viewReservations.show()
        close()

    def deleteReservations2(self):
        self.viewReservations = QtWidgets.QMainWindow()
        self.ui = DR.Ui_viewReservations()
        self.ui.setupUi(self.viewReservations)
        self.viewReservations.show()
        close()


    def back(self):
        self.Admin_Dashboard = QtWidgets.QMainWindow()
        self.ui = AD.Ui_Admin_Dashboard()
        self.ui.setupUi(self.Admin_Dashboard)
        self.Admin_Dashboard.show()
        close()


    def logOut(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = G.Ui_LoginWindow()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        close()

    def setupUi(self, Reservations_Managment):
        Reservations_Managment.setObjectName("Reservations_Managment")
        Reservations_Managment.resize(1200, 600)
        Reservations_Managment.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(Reservations_Managment)
        self.centralwidget.setObjectName("centralwidget")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(10, 30, 71, 61))
        self.logoLabel.setStyleSheet("background-image: url(imageedit_2_5347177992.jpg);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.logOut())
        self.logOutButton.setGeometry(QtCore.QRect(1080, 30, 91, 61))
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
        self.viewButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.showReservations2())
        self.viewButton.setGeometry(QtCore.QRect(190, 430, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.viewButton.setFont(font)
        self.viewButton.setStyleSheet("QPushButton {\n"
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
        self.viewButton.setObjectName("deleteButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.back())
        self.backButton.setGeometry(QtCore.QRect(960, 30, 101, 61))
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
        self.adminDashboardLabel_3.setGeometry(QtCore.QRect(210, 140, 631, 71))
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
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.deleteReservations2())
        self.deleteButton.setGeometry(QtCore.QRect(690, 430, 351, 61))
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
        self.adminDashboardLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_2.setGeometry(QtCore.QRect(220, 240, 651, 71))
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
        Reservations_Managment.setCentralWidget(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1181, 581))
        self.label.setStyleSheet("background-image: url(background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.lower()

        self.statusbar = QtWidgets.QStatusBar(Reservations_Managment)
        self.statusbar.setObjectName("statusbar")
        Reservations_Managment.setStatusBar(self.statusbar)

        self.retranslateUi(Reservations_Managment)
        QtCore.QMetaObject.connectSlotsByName(Reservations_Managment)

    def retranslateUi(self, Reservations_Managment):
        _translate = QtCore.QCoreApplication.translate
        Reservations_Managment.setWindowTitle(_translate("Reservations_Managment", "Reservations Managment"))
        self.viewButton.setText(_translate("Reservations_Managment", "View"))
        self.adminDashboardLabel_3.setText(_translate("Reservations_Managment", "Admin Dashboard"))
        self.deleteButton.setText(_translate("Reservations_Managment", "Delete"))
        self.adminDashboardLabel_2.setText(_translate("Reservations_Managment", "Reservations Mangament"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Reservations_Managment = QtWidgets.QMainWindow()
    ui = Ui_Reservations_Managment()
    ui.setupUi(Reservations_Managment)
    Reservations_Managment.show()
    sys.exit(app.exec_())
