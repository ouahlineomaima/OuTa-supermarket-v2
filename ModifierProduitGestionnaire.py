from PyQt5 import QtCore, QtGui, QtWidgets
from Data import *
from Produit import *
from PyQt5.QtWidgets import *


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def validate(self):
    try:
        oldservice = get_service(Ui_Form.serviceid)
        oldproduct = get_produit(Ui_Form.productid, oldservice)
        name = oldproduct.nom
        qt = oldproduct.quantite
        prix = oldproduct.prix
        maxi = oldproduct.max
        mini = oldproduct.min
        if self.lineEdit.text() != "":
            name = self.lineEdit.text()
        if self.lineEdit_5.text() != "":
            try:
                maxi = int(self.lineEdit_5.text())
            except TypeError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Valeur de max non entière. Veuillez saisir une valeur entière.")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
                return
        if self.lineEdit_6.text() != "":
            try:
                mini = int(self.lineEdit_6.text())
            except TypeError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Valeur de min non entière. Veuillez saisir une valeur entière.")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
                return
        if self.lineEdit_2.text() != "":
            try:
                qt1 = int(self.lineEdit_2.text())
                if qt1 < mini or qt1 > maxi:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)

                    # setting message for Message Box
                    msg.setText("Quantité non valide (hors intervalle). Veuillez saisir une quantité valide.")

                    # setting Message box window title
                    msg.setWindowTitle("Opération échouée")

                    # declaring buttons on Message Box
                    msg.setStandardButtons(QMessageBox.Ok)

                    # start the app
                    retval = msg.exec_()
                    return
                else:
                    qt = qt1
            except TypeError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Valeur de quantité non entière. Veuillez saisir une valeur entière.")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
                return

        if self.lineEdit_4.text() != "":
            try:
                prix = float(self.lineEdit_4.text())
            except TypeError as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Valeur de prix non rèelle. Veuillez saisir une valeur rèelle.")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
                return

        newproduct = Produit(Ui_Form.productid, name, qt, mini, maxi, oldservice, prix)
        if not newproduct.__eq__(oldproduct):
            y = modify_produit(newproduct, oldproduct)
            if y == 1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                # setting message for Message Box
                msg.setText("le produit a été modifié avec succès")

                # setting Message box window title
                msg.setWindowTitle("Opération réussie")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
            elif y == -1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Erreur de la connexion avec la base de données.")

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
            msg.setText("Impossible de modifié le produit. Vous n'avez pas effectué aucun changement.")

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
    serviceid = ""
    productid = ""

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 451)

        self.titlelabel = QtWidgets.QLabel(Form)
        self.titlelabel.setGeometry(QtCore.QRect(0, 0, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titlelabel.setFont(font)
        self.titlelabel.setStyleSheet("color:rgb(255, 255, 255);\n"
                                      "background-color:rgb(13,12,60)")
        self.titlelabel.setObjectName("titlelabel")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 50, 751, 401))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")

        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:4px")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 320, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius:4px")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(360, 80, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:4px")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.nvMaxLabel_2 = QtWidgets.QLabel(Form)
        self.nvMaxLabel_2.setGeometry(QtCore.QRect(150, 320, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nvMaxLabel_2.setFont(font)
        self.nvMaxLabel_2.setStyleSheet("color:rgb(70,68,68)")
        self.nvMaxLabel_2.setObjectName("nvMaxLabel_2")

        self.nvQuantiteLabel = QtWidgets.QLabel(Form)
        self.nvQuantiteLabel.setGeometry(QtCore.QRect(150, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nvQuantiteLabel.setFont(font)
        self.nvQuantiteLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nvQuantiteLabel.setObjectName("nvQuantiteLabel")

        self.nvMinLabel_2 = QtWidgets.QLabel(Form)
        self.nvMinLabel_2.setGeometry(QtCore.QRect(150, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nvMinLabel_2.setFont(font)
        self.nvMinLabel_2.setStyleSheet("color:rgb(70,68,68)")
        self.nvMinLabel_2.setObjectName("nvMinLabel_2")

        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(360, 260, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border-radius:4px")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.nvNomLabel = QtWidgets.QLabel(Form)
        self.nvNomLabel.setGeometry(QtCore.QRect(150, 90, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nvNomLabel.setFont(font)
        self.nvNomLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nvNomLabel.setObjectName("nvNomLabel")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:4px")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.nvPrixLabel = QtWidgets.QLabel(Form)
        self.nvPrixLabel.setGeometry(QtCore.QRect(150, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nvPrixLabel.setFont(font)
        self.nvPrixLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nvPrixLabel.setObjectName("nvPrixLabel")

        self.retourButton = QtWidgets.QPushButton(Form)
        self.retourButton.setGeometry(QtCore.QRect(470, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.retourButton.setFont(font)
        self.retourButton.setStyleSheet("QPushButton{\n"
                                        "background-color:rgb(255, 197, 119);\n"
                                        "color:rgb(255, 255, 255);\n"
                                        "border-radius:4px\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.retourButton.setObjectName("retourButton")
        self.retourButton.clicked.connect(lambda: go_back())

        self.validerButton = QtWidgets.QPushButton(Form)
        self.validerButton.setGeometry(QtCore.QRect(150, 380, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.validerButton.setFont(font)
        self.validerButton.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                         " color:rgb(255, 255, 255);\n"
                                         "border-radius:4px")
        self.validerButton.setObjectName("validerButton")
        self.validerButton.clicked.connect(lambda: validate(self))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.titlelabel.setText(_translate(
            "Form", "          Modifier Un Produit"))
        self.nvMaxLabel_2.setText(_translate("Form", "Nouveau Max:"))
        self.nvQuantiteLabel.setText(_translate("Form", "Nouvelle Quantité:"))
        self.nvMinLabel_2.setText(_translate("Form", "Nouveau Min:"))
        self.nvNomLabel.setText(_translate("Form", "Nouveau Nom:"))
        self.nvPrixLabel.setText(_translate("Form", "Nouveau Prix :"))
        self.retourButton.setText(_translate("Form", "Retour"))
        self.validerButton.setText(_translate("Form", "Valider"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())
