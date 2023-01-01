# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reservation.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from login import gui as G
from tkinter import messagebox

from PyQt5 import QtCore, QtGui, QtWidgets
from main import main_control
import building_Selectionnew as BS
import confirmReservations as CR
from datetime import datetime



class Ui_Reservation(object):

    mc = main_control()


    def logOut(self,Reservation):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = G.Ui_LoginWindow()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        Reservation.close()


    def back(self,Reservation):
        self.BuildingSelection = QtWidgets.QMainWindow()
        self.ui = BS.Ui_BuildingSelection()
        self.ui.setupUi(self.BuildingSelection)
        self.BuildingSelection.show()
        Reservation.close()



    def showConfirm(self,Reservation):
        restuple = []
        dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        restuple.append(dateTime)
        restuple.append(main_control.userInfo[0][0])
        restuple.append(self.floorComboBox.currentText())
        restuple.append(self.buildingIdLabel.text())
        result = self.mc.getGuiMsgsControl()
        if (str(self.mc.confirmRes(restuple)).lower() != 'none'):
            messagebox.showwarning('Warning', str(result[3]))
            return
        self.confrimRes = QtWidgets.QMainWindow()
        self.ui = CR.Ui_viewReservations()
        self.ui.setupUi(self.confrimRes)
        self.confrimRes.show()
        Reservation.close()

    def on_combobox_changed(self, value):
        _translate = QtCore.QCoreApplication.translate
        self.buildingIdLabel.setText(_translate("Reservation",str(self.mc.getBID())))
        self.showNameLabel_2.setText(_translate("Reservation",str(self.mc.getG())))
        result = self.mc.getAvBedsResControl(value)
        self.buildingIdLabel_2.setText(_translate("Reservation",str(result)[11:12]))


    def setupUi(self, Reservation):
        Reservation.setObjectName("Reservation")
        Reservation.resize(1200, 600)
        Reservation.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(Reservation)
        self.centralwidget.setObjectName("centralwidget")
        self.buildingIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.buildingIdLabel.setGeometry(QtCore.QRect(210, 260, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buildingIdLabel.setFont(font)
        self.buildingIdLabel.setStyleSheet("color: rgb(170, 0, 0);")
        self.buildingIdLabel.setText("")
        self.buildingIdLabel.setObjectName("buildingIdLabel")
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(210, 210, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.floorComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.floorComboBox.setGeometry(QtCore.QRect(530, 260, 73, 22))
        self.floorComboBox.setStyleSheet("color: rgb(170, 0, 0);\n")
        self.floorComboBox.setObjectName("floorComboBox")
        self.floorComboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.idLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_2.setGeometry(QtCore.QRect(530, 210, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.idLabel_2.setFont(font)
        self.idLabel_2.setObjectName("idLabel_2")
        self.showNameLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.showNameLabel_2.setGeometry(QtCore.QRect(780, 260, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showNameLabel_2.setFont(font)
        self.showNameLabel_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.showNameLabel_2.setText("")
        self.showNameLabel_2.setObjectName("showNameLabel_2")
        self.idLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_3.setGeometry(QtCore.QRect(780, 205, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.idLabel_3.setFont(font)
        self.idLabel_3.setObjectName("idLabel_3")
        self.ageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel.setGeometry(QtCore.QRect(780, 300, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel.setFont(font)
        self.ageLabel.setObjectName("ageLabel")
        self.buildingIdLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.buildingIdLabel_2.setGeometry(QtCore.QRect(780, 360, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buildingIdLabel_2.setFont(font)
        self.buildingIdLabel_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.buildingIdLabel_2.setText("")
        self.buildingIdLabel_2.setObjectName("buildingIdLabel_2")
        self.adminDashboardLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_2.setGeometry(QtCore.QRect(110, 90, 411, 71))
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
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(20, 10, 71, 61))
        self.logoLabel.setStyleSheet("background-image: url(imageedit_2_5347177992.jpg);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.back(Reservation))
        self.backButton.setGeometry(QtCore.QRect(970, 10, 101, 61))
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
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.logOut(Reservation))
        self.logOutButton.setGeometry(QtCore.QRect(1090, 10, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.logOutButton.setFont(font)
        self.logOutButton.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"image: url(logout.png);\n"

"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"border-radius:6px;\n"
"padding: 10px; \n"
"")
        self.logOutButton.setText("")
        self.logOutButton.setObjectName("logOutButton")
        self.logoLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel_2.setGeometry(QtCore.QRect(850, 200, 41, 31))
        self.logoLabel_2.setStyleSheet("image: url(gender-fluid.png);\n"
"")
        self.logoLabel_2.setText("")
        self.logoLabel_2.setObjectName("logoLabel_2")
        self.logoLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel_3.setGeometry(QtCore.QRect(910, 300, 41, 31))
        self.logoLabel_3.setStyleSheet("image: url(beds.png);\n"
"")
        self.logoLabel_3.setText("")
        self.logoLabel_3.setObjectName("logoLabel_3")
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showConfirm(Reservation))
        self.confirmButton.setGeometry(QtCore.QRect(440, 480, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.confirmButton.setFont(font)
        self.confirmButton.setStyleSheet("QPushButton {\n"
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
        self.confirmButton.setObjectName("confirmButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1181, 581))
        self.label.setStyleSheet("background-image: url(d1668ee13fec4635d7f8d2a65c89d1b2.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.lower()


        Reservation.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Reservation)
        self.statusbar.setObjectName("statusbar")
        Reservation.setStatusBar(self.statusbar)

        self.retranslateUi(Reservation)
        QtCore.QMetaObject.connectSlotsByName(Reservation)
        result = self.mc.getResFloorsControl()
        for item in result:
            self.floorComboBox.addItem(str(item)[1:2])

    def retranslateUi(self, Reservation):
        _translate = QtCore.QCoreApplication.translate
        Reservation.setWindowTitle(_translate("Reservation", "Reservation"))
        self.idLabel.setText(_translate("Reservation", "Building Id"))
        self.idLabel_2.setText(_translate("Reservation", "Choose Floor"))
        self.idLabel_3.setText(_translate("Reservation", "Gender"))
        self.ageLabel.setText(_translate("Reservation", "Avaliable Beds"))
        self.adminDashboardLabel_2.setText(_translate("Reservation", "Bed Reservation"))
        self.confirmButton.setText(_translate("Reservation", "Confirm "))



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Reservation = QtWidgets.QMainWindow()
#     ui = Ui_Reservation()
#     ui.setupUi(Reservation)
#     Reservation.show()
#     sys.exit(app.exec_())
