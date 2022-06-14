from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Data import *
import ajouterProduit
import ModifierProduitGestionnaire
from PyQt5.QtWidgets import *
import profil


def loaddata(self):
    service = get_service(Ui_Form.serviceid)
    productlist = get_allproduit(service)
    row = 0
    self.tableWidget.setRowCount(len(productlist))
    for product in productlist:
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(product.iD))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(product.nom))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(product.quantite)))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(service.nom))
        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(product.prix)))
        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(product.min)))
        self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(product.max)))
        row += 1


def logout():
    Ui_Form.widget.setFixedWidth(Ui_Form.loginwidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.loginheight)
    Ui_Form.widget.setCurrentIndex(0)
    Ui_Form.widget.show()


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def go_to_add_product(self):
    ajouterProduit.Ui_Form.widget = Ui_Form.widget
    ajouterProduit.Ui_Form.previousheight = self.Form.frameGeometry().height()
    ajouterProduit.Ui_Form.previouswidth = self.Form.frameGeometry().width()
    ajouterProduit.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
    ajouterProduit.Ui_Form.serviceid = Ui_Form.serviceid
    addproduct = ajouterProduit.Ui_Form()
    Ui_Form.widget.addWidget(addproduct.Form)
    Ui_Form.widget.setFixedWidth(addproduct.Form.frameGeometry().width())
    Ui_Form.widget.setFixedHeight(addproduct.Form.frameGeometry().height())
    Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)


def delete_product(self):
    item = self.tableWidget.currentItem()
    if item:
        row = self.tableWidget.currentRow()
        productid = self.tableWidget.item(row, 0).text()
        y = delete_produit(productid)
        if y == 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting message for Message Box
            msg.setText("le produit a été supprimé avec succès.")

            # setting Message box window title
            msg.setWindowTitle("Opération réussie")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Erreur de la connexion avec la base de données")

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
        msg.setText("Aucun produit sélectionné. Veuillez sélectionner un produit.")

        # setting Message box window title
        msg.setWindowTitle("Opération échouée")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()


def go_to_modify_product(self):
    item = self.tableWidget.currentItem()
    if item:
        row = self.tableWidget.currentRow()
        productid = self.tableWidget.item(row, 0).text()
        ModifierProduitGestionnaire.Ui_Form.widget = Ui_Form.widget
        ModifierProduitGestionnaire.Ui_Form.previousheight = self.Form.frameGeometry().height()
        ModifierProduitGestionnaire.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        ModifierProduitGestionnaire.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
        ModifierProduitGestionnaire.Ui_Form.serviceid = Ui_Form.serviceid
        ModifierProduitGestionnaire.Ui_Form.productid = productid
        modifyproduct = ModifierProduitGestionnaire.Ui_Form()
        Ui_Form.widget.addWidget(modifyproduct.Form)
        Ui_Form.widget.setFixedWidth(modifyproduct.Form.frameGeometry().width())
        Ui_Form.widget.setFixedHeight(modifyproduct.Form.frameGeometry().height())
        Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("Aucun produit sélectionné. Veuillez sélectionner un produit.")

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
    previousheight = ""
    previouswidth = ""
    previousindex = ""
    loginwidth = ""
    loginheight = ""
    myindex = ""
    serviceid = ""
    gestid = ""

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 320)
        loaddata(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(898, 453)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 898, 55))
        self.label_2.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 55, 898, 453))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(739, 90, 151, 32))
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
        self.pushButton_2.setGeometry(QtCore.QRect(739, 130, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: go_to_add_product(self))

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(739, 170, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: delete_product(self))

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(739, 210, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:rgb(35, 193, 228);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: go_to_modify_product(self))

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 61, 721, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: go_back())

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(logout)

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(737, 8, 150, 42))
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Actualiser"))
        self.pushButton_2.setText(_translate("Form", "Ajouter"))
        self.pushButton_3.setText(_translate("Form", "Supprimer "))
        self.pushButton_4.setText(_translate("Form", "Modifier "))
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
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Min"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Max"))
        self.pushButton_5.setText(_translate("Form", "Retour"))
        self.pushButton_6.setText(_translate("Form", "Se Déconnecter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())
