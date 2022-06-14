from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Data import *
import ajouterProduit
import ModifierProduitAdmin
from PyQt5.QtWidgets import *
import commandeProduit
import profil


def loaddata(self):
    service = get_service(Ui_Form.serviceid)
    productlist = get_allproduit(service)
    row = 0
    self.tableWidget.setRowCount(len(productlist))
    maxspin = 0
    for product in productlist:
        if product.quantite > maxspin:
            maxspin = product.quantite
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(product.iD))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(product.nom))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(product.quantite)))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(service.nom))
        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(product.prix)))
        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(product.min)))
        self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(product.max)))
        row += 1
    self.spinBox.setMaximum(maxspin)


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def logout():
    Ui_Form.widget.setFixedWidth(Ui_Form.loginwidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.loginheight)
    Ui_Form.widget.setCurrentIndex(0)
    Ui_Form.widget.show()


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
        ModifierProduitAdmin.Ui_Form.widget = Ui_Form.widget
        ModifierProduitAdmin.Ui_Form.previousheight = self.Form.frameGeometry().height()
        ModifierProduitAdmin.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        ModifierProduitAdmin.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
        ModifierProduitAdmin.Ui_Form.serviceid = Ui_Form.serviceid
        ModifierProduitAdmin.Ui_Form.productid = productid
        modifyproduct = ModifierProduitAdmin.Ui_Form()
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


def go_to_the_cart(self):
    try:
        commandeProduit.Ui_Form.widget = Ui_Form.widget
        commandeProduit.Ui_Form.previousheight = self.Form.frameGeometry().height()
        commandeProduit.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        commandeProduit.Ui_Form.previousindex = Ui_Form.widget.currentIndex()
        commandeProduit.Ui_Form.loginheight = Ui_Form.loginheight
        commandeProduit.Ui_Form.loginwidth = Ui_Form.loginwidth
        commandeProduit.Ui_Form.gestid = Ui_Form.gestid
        cart = commandeProduit.Ui_Form()
        Ui_Form.widget.addWidget(cart.Form)
        Ui_Form.widget.setFixedWidth(cart.Form.frameGeometry().width())
        Ui_Form.widget.setFixedHeight(cart.Form.frameGeometry().height())
        Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
    except BaseException as e:
        print(e)


def add_to_the_cart(self):
    try:
        item = self.tableWidget.currentItem()
        if item:
            row = self.tableWidget.currentRow()
            service = get_service(Ui_Form.serviceid)
            productid = self.tableWidget.item(row, 0).text()
            originalproduct = get_produit(productid, service)
            x = 0
            spinqt = self.spinBox.value()
            if spinqt != 0:
                if originalproduct.quantite - spinqt > originalproduct.min:
                    for product in commandeProduit.Ui_Form.product_list:
                        if product.iD == "panier"+productid:
                            x = 1
                            break
                    if x == 0:
                        cartproduct = Produit("panier" + productid, originalproduct.nom, spinqt, spinqt - 1, spinqt + 1,
                                              service, originalproduct.prix)
                        commandeProduit.Ui_Form.product_list.append(cartproduct)
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)

                        # setting message for Message Box
                        msg.setText("le produit a été ajouté au panier avec succès")

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
                        msg.setText("Le produit existe déjà dans le panier. Pour modifier sa quantité veuillez le retirer d'abord du panier et le rajouter.")

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
                    msg.setText("Impossible d'ajouter le produit choisi au panier. Veuillez choisir une quantité adéquate.")

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
                msg.setText("Impossible d'ajouter le produit au panier. Veuillez choisir d'abord une quantité.")

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
    previousheight = ""
    previouswidth = ""
    widget = ""
    previousindex = ""
    serviceid = ""
    loginwidth = ""
    loginheight = ""
    gestid = ""

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        loaddata(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(898, 451)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 50, 900, 401))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 900, 55))
        self.label_2.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 10, 111, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: go_back())

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 121, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: go_to_the_cart(self))

        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(270, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: logout())

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(740, 80, 151, 32))
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

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(740, 160, 151, 32))
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
        self.pushButton_4.setGeometry(QtCore.QRect(740, 200, 151, 32))
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

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(740, 120, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: go_to_add_product(self))

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(720, 330, 171, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: add_to_the_cart(self))

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 702, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(780, 370, 61, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")

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
        self.pushButton_8.setText(_translate("Form", "Retour"))
        self.pushButton_2.setText(_translate("Form", "Panier"))
        self.pushButton_9.setText(_translate("Form", "Se Deconnecter"))
        self.pushButton.setText(_translate("Form", "Actualiser"))
        self.pushButton_3.setText(_translate("Form", "Supprimer "))
        self.pushButton_4.setText(_translate("Form", "Modifier "))
        self.pushButton_5.setText(_translate("Form", "Ajouter"))
        self.pushButton_6.setText(_translate("Form", "Ajouter au panier"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())
