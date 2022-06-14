from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from Data import *
from PyQt5.QtWidgets import *
import sys
import serviceGestionnaire
import ajouterService
import Service
import produitAdmin
import profil


def logout(self):
    Ui_Form.widget.setFixedWidth(Ui_Form.loginwidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.loginheight)
    Ui_Form.widget.setCurrentIndex(0)
    Ui_Form.widget.show()


def loaddata(self):
    serviceList = get_allservice()
    row = 0
    self.tableWidget.setRowCount(len(serviceList))
    for service in serviceList:
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(service.iD))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(service.nom))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(service.gestionnaire.nom_complet))
        row += 1


def go_to_gest():
    serviceGestionnaire.Ui_Form.widget = Ui_Form.widget
    serviceGestionnaire.Ui_Form.loginheight = Ui_Form.loginheight
    serviceGestionnaire.Ui_Form.loginwidth = Ui_Form.loginwidth
    serviceGestionnaire.Ui_Form.gestid = Ui_Form.gestid
    tablegestui = serviceGestionnaire.Ui_Form()
    serviceGestionnaire.Ui_Form.serviceheight = tablegestui.Form.frameGeometry().height()
    serviceGestionnaire.Ui_Form.servicewidth = tablegestui.Form.frameGeometry().width()
    Ui_Form.widget.addWidget(tablegestui.Form)
    serviceGestionnaire.Ui_Form.myindex = Ui_Form.widget.__len__() - 1
    serviceGestionnaire.Ui_Form.serviceindex = Ui_Form.widget.currentIndex()
    Ui_Form.widget.setFixedWidth(tablegestui.Form.frameGeometry().width())
    Ui_Form.widget.setFixedHeight(tablegestui.Form.frameGeometry().height())
    Ui_Form.widget.setCurrentIndex(tablegestui.myindex)


def go_to_add_service(self):
    ajouterService.Ui_Form.widget = Ui_Form.widget
    ajouterService.Ui_Form.previousheight = self.Form.frameGeometry().height()
    ajouterService.Ui_Form.previouswidth = self.Form.frameGeometry().width()
    ajouterService.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
    addservice = ajouterService.Ui_Form()
    Ui_Form.widget.addWidget(addservice.Form)
    Ui_Form.widget.setFixedWidth(addservice.Form.frameGeometry().width())
    Ui_Form.widget.setFixedHeight(addservice.Form.frameGeometry().height())
    Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)


def delete_service(self):
    item = self.tableWidget.currentItem()
    if item is not None:
        print(item)
        row = self.tableWidget.currentRow()
        serviceid = self.tableWidget.item(row, 0).text()
        servicename = self.tableWidget.item(row, 1).text()
        servicegestname = self.tableWidget.item(row, 2).text()
        if serviceid != "00":
            admin = get_gestionnaire("0000")
            service = get_service(serviceid)
            defaultservice = get_service("00")
            productlist = get_allproduit(service)
            if productlist:
                for product in productlist:
                    product.set_service(defaultservice)
            if admin.supprimer_service(serviceid) == 1:  # all is good
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                # setting message for Message Box
                msg.setText("Le service a été supprimé avec succès.")

                # setting Message box window title
                msg.setWindowTitle("Opération réussie")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
            else:  # database connection error
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Erreur de la connection avec la base de données.")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
        else:  # can't delete default service
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Impossible de supprimer le service par défaut. Veuillez sélectionner un autre service")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("Aucun service sélectionné. Veuillez sélectionner un service d'abord.")

        # setting Message box window title
        msg.setWindowTitle("Opération échouée")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()


def consult(self):
    item = self.tableWidget.currentItem()
    if item is not None:
        row = self.tableWidget.currentRow()
        produitAdmin.Ui_Form.serviceid = self.tableWidget.item(row, 0).text()
        produitAdmin.Ui_Form.widget = Ui_Form.widget
        produitAdmin.Ui_Form.previousheight = self.Form.frameGeometry().height()
        produitAdmin.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        produitAdmin.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
        produitAdmin.Ui_Form.loginheight = Ui_Form.loginheight
        produitAdmin.Ui_Form.loginwidth = Ui_Form.loginwidth
        produitAdmin.Ui_Form.gestid = Ui_Form.gestid
        showproduct = produitAdmin.Ui_Form()
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
    profil.Ui_Form.widget = Ui_Form.widget
    profil.Ui_Form.previousheight = self.Form.frameGeometry().height()
    profil.Ui_Form.previouswidth = self.Form.frameGeometry().width()
    profil.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
    profil.Ui_Form.gestid = Ui_Form.gestid
    profile = profil.Ui_Form()
    Ui_Form.widget.addWidget(profile.Form)
    Ui_Form.widget.setFixedWidth(profile.Form.frameGeometry().width())
    Ui_Form.widget.setFixedHeight(profile.Form.frameGeometry().height())
    Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)


class Ui_Form(object):
    widget = ""
    loginheight = ""
    loginwidth = ""
    gestid = "0000"

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 220)
        self.tableWidget.setColumnWidth(2, 230)
        loaddata(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 451)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 60, 751, 391))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 561, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(590, 80, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(35, 193, 228);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: loaddata(self))

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 120, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(85, 255, 0);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: go_to_add_service(self))

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 160, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 197, 119);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: delete_service(self))

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 200, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:rgb(35, 193, 228);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: consult(self))

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 751, 55))
        self.label_2.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color:rgb(35, 193, 228);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color:rgb(217, 217, 217);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: go_to_gest())

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(330, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color:rgb(255, 197, 119);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(logout)

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(590, 10, 150, 42))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:rgb(35, 193, 228);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_5.setText("Profil")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setIcon(QIcon("profil1.png"))
        self.pushButton_5.setIconSize(QSize(50, 50))
        self.pushButton_5.clicked.connect(lambda: go_to_profil(self))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Service"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nom Gestionnaire"))
        self.pushButton.setText(_translate("Form", "Actualiser"))
        self.pushButton_2.setText(_translate("Form", "Ajouter"))
        self.pushButton_3.setText(_translate("Form", "Supprimer "))
        self.pushButton_4.setText(_translate("Form", "Consulter "))
        self.pushButton_6.setText(_translate("Form", "Services"))
        self.pushButton_7.setText(_translate("Form", "Gestionnaires"))
        self.pushButton_8.setText(_translate("Form", "Se Déconnecter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())
