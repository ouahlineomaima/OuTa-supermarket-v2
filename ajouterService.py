from PyQt5 import QtCore, QtGui, QtWidgets
from Data import *
from Service import *
from PyQt5.QtWidgets import *


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def validate(self):
    serviceid = self.lineEdit_2.text()
    servicename = self.lineEdit_3.text()
    gestid = self.lineEdit_4.text()
    service = get_service(serviceid)
    if service is None:
        x = 0
        for oldservice in get_allservice():
            if servicename == oldservice.nom:
                x = 1
                break
        if x == 0:
            gest = get_gestionnaire(gestid)
            if gest is not None:
                admin = get_gestionnaire("0000")
                newservice = Service(serviceid, servicename, gest)
                if admin.ajouter_service(newservice) == 1:  # all is good
                    self.lineEdit_2.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)

                    # setting message for Message Box
                    msg.setText("le service a été ajouté avec succès")

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
                    msg.setText("Erreur de la connexion avec la base de données")

                    # setting Message box window title
                    msg.setWindowTitle("Opération échouée")

                    # declaring buttons on Message Box
                    msg.setStandardButtons(QMessageBox.Ok)

                    # start the app
                    retval = msg.exec_()
            else:  # no manager with the mentioned id
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Aucun gestionnaire ne correspond à l'id saisi.")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
        else:  # name already existent
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Le nom saisi figure déjà dans la base de données. Veuillez choisir un autre nom")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
    else:  # id already existent
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("L'id saisi figure déjà dans la base de données. Veuillez choisir un autre id.")

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

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 488)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 751, 441))
        self.label_2.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(338, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 4px")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(338, 240, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:4px")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(338, 180, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:4px")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.nomLabel = QtWidgets.QLabel(Form)
        self.nomLabel.setGeometry(QtCore.QRect(157, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nomLabel.setFont(font)
        self.nomLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nomLabel.setObjectName("nomLabel")

        self.IdGestionnaireLabel = QtWidgets.QLabel(Form)
        self.IdGestionnaireLabel.setGeometry(QtCore.QRect(157, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.IdGestionnaireLabel.setFont(font)
        self.IdGestionnaireLabel.setStyleSheet("color:rgb(70,68,68)")
        self.IdGestionnaireLabel.setObjectName("IdGestionnaireLabel")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 310, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 197, 119);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: go_back())

        self.idServiceLabel = QtWidgets.QLabel(Form)
        self.idServiceLabel.setGeometry(QtCore.QRect(157, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idServiceLabel.setFont(font)
        self.idServiceLabel.setStyleSheet("color:rgb(70,68,68)")
        self.idServiceLabel.setObjectName("idServiceLabel")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 310, 151, 32))
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

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(13,12,60)")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nomLabel.setText(_translate("Form", "Nom:"))
        self.IdGestionnaireLabel.setText(_translate("Form", "ID Gestionnaire:"))
        self.pushButton_2.setText(_translate("Form", "Retour"))
        self.idServiceLabel.setText(_translate("Form", "ID Service:"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.label_3.setText(_translate("Form", "Ajouter Un Service"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())

