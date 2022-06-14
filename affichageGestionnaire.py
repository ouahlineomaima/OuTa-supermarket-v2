from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Data import *
from PyQt5.QtWidgets import *
import produitGestionnaire
import profil


def logout(self):
    Ui_Form.widget.setFixedWidth(Ui_Form.loginwidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.loginheight)
    Ui_Form.widget.setCurrentIndex(0)
    Ui_Form.widget.show()


def consult(self):
    item = self.tableWidget.currentItem()
    if item is not None:
        row = self.tableWidget.currentRow()
        produitGestionnaire.Ui_Form.serviceid = self.tableWidget.item(row, 0).text()
        produitGestionnaire.Ui_Form.widget = Ui_Form.widget
        produitGestionnaire.Ui_Form.previousheight = self.Form.frameGeometry().height()
        produitGestionnaire.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        produitGestionnaire.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
        produitGestionnaire.Ui_Form.loginheight = Ui_Form.loginheight
        produitGestionnaire.Ui_Form.loginwidth = Ui_Form.loginwidth
        produitGestionnaire.Ui_Form.gestid = Ui_Form.gest_id
        showproduct = produitGestionnaire.Ui_Form()
        Ui_Form.widget.addWidget(showproduct.Form)
        Ui_Form.widget.setFixedWidth(showproduct.Form.frameGeometry().width())
        Ui_Form.widget.setFixedHeight(showproduct.Form.frameGeometry().height())
        Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("Aucun service sélectionné. Veuillez sélectionner d'abord un service.")

        # setting Message box window title
        msg.setWindowTitle("Opération échouée")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()


def go_to_profil(self):
    try:
        profil.Ui_Form.widget = Ui_Form.widget
        profil.Ui_Form.previousheight = self.Form.frameGeometry().height()
        profil.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        profil.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
        profil.Ui_Form.gestid = Ui_Form.gest_id
        profile = profil.Ui_Form()
        Ui_Form.widget.addWidget(profile.Form)
        Ui_Form.widget.setFixedWidth(profile.Form.frameGeometry().width())
        Ui_Form.widget.setFixedHeight(profile.Form.frameGeometry().height())
        Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
    except BaseException as e:
        print(e)


class Ui_Form(object):
    gest_id = ""
    widget = ""
    loginheight = ""
    loginwidth = ""

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 371)
        self.loaddata()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 451)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 761, 451))
        self.label_2.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(610, 120, 131, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(85, 255, 0);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: consult(self))

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 751, 55))
        self.label_3.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color:rgb(255, 197, 119);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(logout)

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 571, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(590, 10, 150, 42))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color:rgb(35, 193, 228);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_7.setText("Profil")
        self.pushButton_7.setObjectName("pushButton_5")
        self.pushButton_7.setIcon(QIcon("profil1.png"))
        self.pushButton_7.setIconSize(QSize(50, 50))
        self.pushButton_7.clicked.connect(lambda: go_to_profil(self))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def loaddata(self):
        serviceList = get_gest_services(Ui_Form.gest_id)
        row = 0
        self.tableWidget.setRowCount(len(serviceList))
        for service in serviceList:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(service.iD))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(service.nom))
            row += 1

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Consulter"))
        self.pushButton_9.setText(_translate("Form", "Se Déconnecter"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Service"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nom"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())

