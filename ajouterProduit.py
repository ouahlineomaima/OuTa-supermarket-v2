from PyQt5 import QtCore, QtGui, QtWidgets
from Data import *
from Produit import *
from PyQt5.QtWidgets import *


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def validate(self):
    productid = self.lineEdit.text()
    productname = self.lineEdit_2.text()
    productqt = self.lineEdit_3.text()
    productprice = self.lineEdit_4.text()
    productmin = self.lineEdit_5.text()
    productmax = self.lineEdit_6.text()
    cursor, db = get_connection()
    request = "SELECT idproduit FROM produit"
    cursor.execute(request)
    x = 0
    list = cursor.fetchall()
    try:
        for i in range(len(list)):
            id = list[i][0]
            if id == productid:
                x = 1
                break
    except BaseException as e:
        print(e)
    if x == 0:  # unique id
        try:
            if int(productqt) >= int(productmin) and int(productqt) <= int(productmax):
                service = get_service(Ui_Form.serviceid)
                product = Produit(productid, productname, productqt, productmin, productmax, service, productprice)
                y = add_produit(product, service)
                if y == 1:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)

                    # setting message for Message Box
                    msg.setText("le produit a été ajouté avec succès.")

                    # setting Message box window title
                    msg.setWindowTitle("Opération réussie")

                    # declaring buttons on Message Box
                    msg.setStandardButtons(QMessageBox.Ok)

                    # start the app
                    retval = msg.exec_()
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_6.setText("")
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
                msg.setText("Quantité invalide. Veuillez saisir une quantité entre le min et le max.")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
        except BaseException as e:
            print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Valeur non entière pour la quantité, le minimum, le maximum, ou le prix.")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
    else:  # already existant id
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("L'id saisi figure déjà dans la base de données. Veuillez choisir un autre.")

        # setting Message box window title
        msg.setWindowTitle("Opération échouée")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()


class Ui_Form(object):
    previousheight = ""
    previouswidth = ""
    widget = ""
    previousindex = ""
    serviceid = ""

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 500)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 40, 751, 500))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(13,12,60)")
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)  #id
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 131, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:4px")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_4 = QtWidgets.QLineEdit(Form)  #prix
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 233, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:4px")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)  #qt
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 182, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:4px")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.quantiteLabel = QtWidgets.QLabel(Form)
        self.quantiteLabel.setGeometry(QtCore.QRect(159, 182, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.quantiteLabel.setFont(font)
        self.quantiteLabel.setStyleSheet("color:rgb(70,68,68)")
        self.quantiteLabel.setObjectName("quantiteLabel")

        self.prixLabel = QtWidgets.QLabel(Form)
        self.prixLabel.setGeometry(QtCore.QRect(159, 233, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.prixLabel.setFont(font)
        self.prixLabel.setStyleSheet("color:rgb(70,68,68)")
        self.prixLabel.setObjectName("prixLabel")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(405, 404, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 197, 119);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:4px\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: go_back())

        self.nomLabel = QtWidgets.QLabel(Form)
        self.nomLabel.setGeometry(QtCore.QRect(159, 131, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nomLabel.setFont(font)
        self.nomLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nomLabel.setObjectName("nomLabel")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(175, 404, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(85, 255, 0);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: validate(self) )

        self.idProduitLabel = QtWidgets.QLabel(Form)
        self.idProduitLabel.setGeometry(QtCore.QRect(159, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idProduitLabel.setFont(font)
        self.idProduitLabel.setStyleSheet("color:rgb(70,68,68)")
        self.idProduitLabel.setObjectName("idProduitLabel")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(340, 80, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:4px")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 284, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius:4px")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit")

        self.minLabel = QtWidgets.QLabel(Form)
        self.minLabel.setGeometry(QtCore.QRect(159, 284, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.minLabel.setFont(font)
        self.minLabel.setStyleSheet("color:rgb(70,68,68)")
        self.minLabel.setObjectName("idProduitLabel")

        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(340, 335, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border-radius:4px")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit")

        self.maxLabel = QtWidgets.QLabel(Form)
        self.maxLabel.setGeometry(QtCore.QRect(159, 335, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.maxLabel.setFont(font)
        self.maxLabel.setStyleSheet("color:rgb(70,68,68)")
        self.maxLabel.setObjectName("idProduitLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "          Ajouter Un Produit"))
        self.quantiteLabel.setText(_translate("Form", "Quantité:"))
        self.prixLabel.setText(_translate("Form", "Prix Unitaire:"))
        self.pushButton_2.setText(_translate("Form", "Retour"))
        self.nomLabel.setText(_translate("Form", "Nom:"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.idProduitLabel.setText(_translate("Form", "ID Produit:"))
        self.minLabel.setText(_translate("Form", "Minimum :"))
        self.maxLabel.setText(_translate("Form", "Maximum :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())

