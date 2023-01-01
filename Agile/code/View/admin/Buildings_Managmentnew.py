# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Buildings_Managment.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import addNewBuildingsnew as addB
import modifyBuildingnew as MD
import deleteBuildingnew as DB
import Admin_Dashboardnew as AD
from login import gui as G


def close():
    Buildings_Managment.close()
    pass

class Ui_Buildings_Managment(object):

    def showaddNewBuildings(self):
        self.addNewBuildingsnew = QtWidgets.QMainWindow()
        self.ui = addB.Ui_addNewBuilding()
        self.ui.setupUi(self.addNewBuildingsnew)
        self.addNewBuildingsnew.show()
        close()


    def showmodifyBuilding(self):
        self.modifyBuilding = QtWidgets.QMainWindow()
        self.ui = MD.Ui_modifyBuilding()
        self.ui.setupUi(self.modifyBuilding)
        self.modifyBuilding.show()
        close()



    def showdeleteBuilding(self):
        self.deleteBuilding = QtWidgets.QMainWindow()
        self.ui = DB.Ui_deleteBuilding()
        self.ui.setupUi(self.deleteBuilding)
        self.deleteBuilding.show()
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


    def setupUi(self, Buildings_Managment):
        Buildings_Managment.setObjectName("Buildings_Managment")
        Buildings_Managment.resize(1200, 600)
        Buildings_Managment.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(Buildings_Managment)
        self.centralwidget.setObjectName("centralwidget")
        self.showResidentInfoPushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.back())
        self.showResidentInfoPushButton_3.setGeometry(QtCore.QRect(970, 20, 101, 61))
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
        self.logoLabel.setGeometry(QtCore.QRect(20, 20, 71, 61))
        self.logoLabel.setStyleSheet("background-image: url(imageedit_2_5347177992.jpg);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.showResidentInfoPushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.logOut())
        self.showResidentInfoPushButton_2.setGeometry(QtCore.QRect(1090, 20, 91, 61))
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
        self.idLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_2.setGeometry(QtCore.QRect(805, 230, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_2.setFont(font)
        self.idLabel_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(home.png);")
        self.idLabel_2.setText("")
        self.idLabel_2.setObjectName("idLabel_2")
        self.adminDashboardLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_2.setGeometry(QtCore.QRect(280, 230, 511, 71))
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
        self.adminDashboardLabel_3.setGeometry(QtCore.QRect(220, 130, 631, 71))
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
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showaddNewBuildings())
        self.addButton.setGeometry(QtCore.QRect(60, 420, 351, 61))
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
                                     "}")
        self.addButton.setObjectName("addButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showdeleteBuilding())
        self.deleteButton.setGeometry(QtCore.QRect(830, 420, 351, 61))
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
                                     "}")
        self.deleteButton.setObjectName("deleteButton")
        self.modifyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showmodifyBuilding())
        self.modifyButton.setGeometry(QtCore.QRect(450, 420, 351, 61))
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
                                     "}")
        self.modifyButton.setObjectName("modifyButton")
        Buildings_Managment.setCentralWidget(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1181, 581))
        self.label.setStyleSheet("background-image: url(background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.lower()

        self.statusbar = QtWidgets.QStatusBar(Buildings_Managment)
        self.statusbar.setObjectName("statusbar")
        Buildings_Managment.setStatusBar(self.statusbar)

        self.retranslateUi(Buildings_Managment)
        QtCore.QMetaObject.connectSlotsByName(Buildings_Managment)

    def retranslateUi(self, Buildings_Managment):
        _translate = QtCore.QCoreApplication.translate
        Buildings_Managment.setWindowTitle(_translate("Buildings_Managment", "BuildingsManagment"))
        self.adminDashboardLabel_2.setText(_translate("Buildings_Managment", "Building Managment"))
        self.adminDashboardLabel_3.setText(_translate("Buildings_Managment", "Admin Dashboard"))
        self.addButton.setText(_translate("Buildings_Managment", "Add "))
        self.deleteButton.setText(_translate("Buildings_Managment", "Delete"))
        self.modifyButton.setText(_translate("Buildings_Managment", "Modify"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Buildings_Managment = QtWidgets.QMainWindow()
    ui = Ui_Buildings_Managment()
    ui.setupUi(Buildings_Managment)
    Buildings_Managment.show()
    sys.exit(app.exec_())
