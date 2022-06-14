from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Data import *
import ajouterGestionnaire
from PyQt5.QtWidgets import *
import affecterService
import profil


def loaddata(self):
    gestList = get_allgestionnaire()
    row = 0
    self.tableWidget.setRowCount(len(gestList))
    for gest in gestList:
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(gest.id))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(gest.nom_complet))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(gest.telephone))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(gest.address))
        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(gest.email))
        row += 1


def logout():
    Ui_Form.widget.setFixedWidth(Ui_Form.loginwidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.loginheight)
    Ui_Form.widget.setCurrentIndex(0)
    Ui_Form.widget.show()


def go_to_service():
    Ui_Form.widget.setFixedWidth(Ui_Form.servicewidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.serviceheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.serviceindex)
    Ui_Form.widget.show()


def go_to_add_manager(self):
    ajouterGestionnaire.Ui_Form.widget = Ui_Form.widget
    ajouterGestionnaire.Ui_Form.previousheight = self.Form.frameGeometry().height()
    ajouterGestionnaire.Ui_Form.previouswidth = self.Form.frameGeometry().width()
    ajouterGestionnaire.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
    addmanager = ajouterGestionnaire.Ui_Form()
    Ui_Form.widget.addWidget(addmanager.Form)
    Ui_Form.widget.setFixedWidth(addmanager.Form.frameGeometry().width())
    Ui_Form.widget.setFixedHeight(addmanager.Form.frameGeometry().height())
    Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)


def delete_manager(self):
    item = self.tableWidget.currentItem()
    row = self.tableWidget.currentRow()
    gestid = self.tableWidget.item(row, 0).text()
    if item is not None:
        if gestid != "0000":
            admin = get_gestionnaire("0000")
            if admin.supprimer_gestionnaire(gestid) == 1:  # all is good
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                # setting message for Message Box
                msg.setText("Le gestionnaire a été supprimé avec succès.")

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
        else:  # can't delete default admin
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Impossible de supprimer l'admin. Veuillez sélectionner un autre gestionnaire")

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
        msg.setText("Aucun gestionnaire sélectionné. Veuillez sélectionner gestionnaire d'abord. ")

        # setting Message box window title
        msg.setWindowTitle("Opération échouée")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()


def go_to_assign_manager(self):
    try:
        affecterService.Ui_Form.widget = Ui_Form.widget
        assignmanager = affecterService.Ui_Form()
        affecterService.Ui_Form.previousheight = self.Form.frameGeometry().height()
        affecterService.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        affecterService.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
        item = self.tableWidget.currentItem()
        if item is not None:
            row = self.tableWidget.currentRow()
            affecterService.Ui_Form.gest_id = self.tableWidget.item(row, 0).text()
            Ui_Form.widget.addWidget(assignmanager.Form)
            Ui_Form.widget.setFixedWidth(assignmanager.Form.frameGeometry().width())
            Ui_Form.widget.setFixedHeight(assignmanager.Form.frameGeometry().height())
            Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Aucun gestionnaire sélectionné. Veuillez sélectionner d'abord un gestionnaire.")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
    except BaseException as e:
        print(e)


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
    serviceheight = ""
    servicewidth = ""
    myindex = ""
    serviceindex = ""
    gestid = ""

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
        self.label.setGeometry(QtCore.QRect(0, 50, 751, 401))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 751, 55))
        self.label_2.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color:rgb(35, 193, 228);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_7.setObjectName("pushButton_7")

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

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color:rgb(217, 217, 217);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: go_to_service())

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 170, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: delete_manager(self))

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 210, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:rgb(35, 193, 228);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: go_to_assign_manager(self))

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 130, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: go_to_add_manager(self))

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(590, 90, 151, 32))
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

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 551, 361))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)

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
        self.pushButton_7.setText(_translate("Form", "Gestionnaires"))
        self.pushButton_8.setText(_translate("Form", "Se Déconnecter"))
        self.pushButton_6.setText(_translate("Form", "Services"))
        self.pushButton_3.setText(_translate("Form", "Supprimer "))
        self.pushButton_4.setText(_translate("Form", "Affecter à un service "))
        self.pushButton_2.setText(_translate("Form", "Ajouter"))
        self.pushButton.setText(_translate("Form", "Actualiser"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Gestionnaire"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nom Complet"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Téléphone"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Adresse"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "E-mail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())
