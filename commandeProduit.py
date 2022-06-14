from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Data import *
from PyQt5.QtWidgets import *
import profil
from Commande import Commande
import exporterCommande


def loaddata(self):
    row = 0
    self.tableWidget.setRowCount(len(Ui_Form.product_list))
    for produit in Ui_Form.product_list:
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(produit.iD[6:]))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(produit.nom))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(produit.quantite)))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(produit.service.nom))
        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(produit.prix)))
        row += 1


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def logout():
    Ui_Form.widget.setFixedWidth(Ui_Form.loginwidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.loginheight)
    Ui_Form.widget.setCurrentIndex(0)
    Ui_Form.widget.show()


def go_to_profil(self):
    try:
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
    except BaseException as e:
        print(e)


def remove_from_cart(self):
    item = self.tableWidget.currentItem()
    if item:
        row = self.tableWidget.currentRow()
        Ui_Form.product_list.pop(row)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("le produit a été retiré avec succès.")

        # setting Message box window title
        msg.setWindowTitle("Opération réussie")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()
        loaddata(self)
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("Aucun produit sélectionné. Veuillez sélectionner d'abord un produit.")

        # setting Message box window title
        msg.setWindowTitle("Opération échouée")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()


def validate(self):
    try:
        if Ui_Form.product_list != []:
            productmap = {}
            for produit in Ui_Form.product_list:
                productmap.update({produit: produit.quantite})
            cmdid = int(get_last_commande_id()) + 1
            cmd = Commande(cmdid, productmap)
            cmd.achat_produit()
            commit_commande(cmd)
            Ui_Form.export_product_list = Ui_Form.product_list
            Ui_Form.product_list = []
            Ui_Form.validated = True
            exporterCommande.Ui_Form.exported = False

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting message for Message Box
            msg.setText("la commande a été validée avec succès.")

            # setting Message box window title
            msg.setWindowTitle("Opération réussie")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
            loaddata(self)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("la commande a déjà été validée.")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
            return

    except BaseException as e:
        print(e)


def go_to_export(self):
    try:
        if Ui_Form.validated:
            if not exporterCommande.Ui_Form.exported:
                exporterCommande.Ui_Form.widget = Ui_Form.widget
                exporterCommande.Ui_Form.previousheight = self.Form.frameGeometry().height()
                exporterCommande.Ui_Form.previouswidth = self.Form.frameGeometry().width()
                exporterCommande.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
                exporterCommande.Ui_Form.export_product_list = Ui_Form.export_product_list
                export = exporterCommande.Ui_Form()
                Ui_Form.widget.addWidget(export.Form)
                Ui_Form.widget.setFixedWidth(export.Form.frameGeometry().width())
                Ui_Form.widget.setFixedHeight(export.Form.frameGeometry().height())
                Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Impossible d'exporter la commande. la commande a déjà été exportée.")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
                return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Impossible d'exporter la commande. Veuillez la valider d'abord.")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
            return
    except BaseException as e:
        print(e)


class Ui_Form(object):
    previousheight = ""
    previouswidth = ""
    widget = ""
    previousindex = ""
    product_list = []
    export_product_list = []
    loginwidth = ""
    loginheight = ""
    gestid = ""
    validated = False

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        loaddata(self)
        if exporterCommande.clear() == 0:
            Ui_Form.export_product_list = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 451)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 761, 451))
        self.label_2.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 751, 55))
        self.label_3.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 181, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(85, 255, 0);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: go_to_export(self))

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(207, 10, 111, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color:rgb(255, 197, 119);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: go_back())

        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(327, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color:rgb(255, 197, 119);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: logout())

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(565, 100, 181, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(85, 255, 0);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: validate(self))

        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(580, 140, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color:rgb(255, 197, 119);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda: remove_from_cart(self))

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 551, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
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
        self.pushButton_2.setText(_translate("Form", "Exporter La commande"))
        self.pushButton_8.setText(_translate("Form", "Retour"))
        self.pushButton_9.setText(_translate("Form", "Se Déconnecter"))
        self.pushButton_3.setText(_translate("Form", "Valider La commande"))
        self.pushButton_10.setText(_translate("Form", "Retirer Produit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Produit"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Quantite"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Service"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Prix Unitaire"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())

