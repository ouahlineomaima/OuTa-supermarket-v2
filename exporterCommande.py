from PyQt5 import QtCore, QtGui, QtWidgets
from Data import *
from PyQt5.QtWidgets import *


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def validate(self):
    try:
        if not Ui_Form.exported:
            lastid = get_last_commande_id()
            text = self.lineEdit.text()
            filename = f"{text}\commande{lastid}.txt"
            total_global = 0
            x = len(Ui_Form.export_product_list)
            if x:
                for i in range(x):
                    file = open(filename, "at")
                    nom = Ui_Form.export_product_list[i].nom
                    qt = Ui_Form.export_product_list[i].quantite
                    prix = Ui_Form.export_product_list[i].prix
                    total_unitaire = qt * prix
                    total_global += total_unitaire
                    service = Ui_Form.export_product_list[i].service.nom
                    msg = f"Produit N°{i}: {nom} | service: {service} | quantité: {qt} | prix unitaire: {prix} | prix total: {total_unitaire} \n"
                    file.write(msg)
                    file.close()
                file = open(filename, "at")
                msg = f"Total global: {total_global}"
                file.write(msg)
                file.close()
                Ui_Form.export_product_list = []
                Ui_Form.exported = True
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                # setting message for Message Box
                msg.setText("la commande a été exportée avec succès.")

                # setting Message box window title
                msg.setWindowTitle("Opération réussie")

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
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("la commande a déjà été exportée.")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
            return
    except FileNotFoundError as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("Impossible d'exporter la commande. Veuillez saisir un chemin valide")

        # setting Message box window title
        msg.setWindowTitle("Opération échouée")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()
        return


def default_path(self):
    try:
        if not Ui_Form.exported:
            lastid = get_last_commande_id()
            filename = f"commande{lastid}.txt"
            total_global = 0
            x = len(Ui_Form.export_product_list)
            if x:
                for i in range(x):
                    file = open(filename, "at")
                    nom = Ui_Form.export_product_list[i].nom
                    qt = Ui_Form.export_product_list[i].quantite
                    prix = Ui_Form.export_product_list[i].prix
                    total_unitaire = qt * prix
                    total_global += total_unitaire
                    service = Ui_Form.export_product_list[i].service.nom
                    msg = f"Produit N°{i}: {nom}, service: {service}, quantité: {qt}, prix unitaire: {prix}, prix total: {total_unitaire} \n"
                    file.write(msg)
                    file.close()
                file = open(filename, "at")
                msg = f"Total global: {total_global}"
                file.write(msg)
                file.close()
                Ui_Form.export_product_list = []
                Ui_Form.exported = True
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                # setting message for Message Box
                msg.setText("la commande a été exportée avec succès.")

                # setting Message box window title
                msg.setWindowTitle("Opération réussie")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
                return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("La commande a déjà été exportée.")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
            return
    except FileNotFoundError as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("Impossible d'exporter la commande. Veuillez saisir un chemin valide")

        # setting Message box window title
        msg.setWindowTitle("Opération échouée")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()
        return


def clear():
    if Ui_Form.exported:
        return 0
    return -1


class Ui_Form(object):
    export_product_list = []
    previousheight = ""
    previouswidth = ""
    widget = ""
    previousindex = ""
    exported = False

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 349)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 600, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "background-color:rgb(13,12,60)")
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 50, 600, 300))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 170, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:4px")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 220, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                      " color:rgb(255, 255, 255);\n"
                                      "border-radius:4px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: validate(self))

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 260, 191, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: default_path(self))

        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(200, 300, 191, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_20.setObjectName("pushButton_2")
        self.pushButton_20.clicked.connect(lambda: go_back())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate(
            "Form", "          Exporter La Commande"))
        self.label_3.setText(_translate(
            "Form", "Veuillez inserer le chemin absolu du dossier d’exportation"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.pushButton_2.setText(_translate("Form", "Dossier Par Défaut"))
        self.pushButton_20.setText(_translate("Form", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())
