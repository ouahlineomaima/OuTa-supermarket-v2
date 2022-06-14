from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Data import *
import hashlib
import smtplib


def send_email(msg, destination):
    try:
        sender_email = "OuTasupermarket@gmail.com"
        password = "sfjtqhbqxcxhpqrt"
        reciever_email = destination
        server = smtplib.SMTP("smtp.gmail.com", 587, "127.0.0.1")
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_email, msg)
        server.quit()
    except BaseException as e:
        print(e)


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def validate(self):
    try:
        gestid = self.lineEdit.text()
        gestname = self.lineEdit_2.text()
        gesttele = self.lineEdit_3.text()
        gestaddress = self.lineEdit_4.text()
        gestemail = self.lineEdit_5.text()
        gest = get_gestionnaire(gestid)
        if gest is None:
            x = 0
            for oldgest in get_allgestionnaire():
                if gestname == oldgest.nom_complet:
                    x = 1
                    break
            if x == 0:
                admin = get_gestionnaire("0000")
                nonencodedpass = gestid + gestname
                passwd = hashlib.md5(nonencodedpass.encode()).hexdigest()
                if admin.ajouter_gestionnaire(gestid, gestname, gesttele, gestaddress, gestemail, passwd) == 1:  # all is good
                    message = f"""Congratulation {gestname}
Vous etes desormais partie de l'equipe OuTa supermarket.
votre id {gestid}
votre password par default {gestid + gestname}
Veuillez changer votre password par default le plus tot possible.
Cordialement,"""
                    destination = gestemail
                    send_email(message, destination)
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_5.setText("")
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)

                    # setting message for Message Box
                    msg.setText("le gestionnaire a été ajouté avec succès")

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

            else:  # name or email already existent
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Le nom saisi figure déjà dans la base de données. Veuillez saisir un autre nom.")

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
    except BaseException as e:
        print(e)


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

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(13,12,60)")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 751, 441))
        self.label_2.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(308, 110, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:4px")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(308, 232, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:4px")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.nomLabel = QtWidgets.QLabel(Form)
        self.nomLabel.setGeometry(QtCore.QRect(127, 171, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nomLabel.setFont(font)
        self.nomLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nomLabel.setObjectName("nomLabel")

        self.TeleLabel = QtWidgets.QLabel(Form)
        self.TeleLabel.setGeometry(QtCore.QRect(127, 232, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TeleLabel.setFont(font)
        self.TeleLabel.setStyleSheet("color:rgb(70,68,68)")
        self.TeleLabel.setObjectName("TeleLabel")

        self.idLabel = QtWidgets.QLabel(Form)
        self.idLabel.setGeometry(QtCore.QRect(127, 120, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idLabel.setFont(font)
        self.idLabel.setStyleSheet("color:rgb(70,68,68)")
        self.idLabel.setObjectName("idLabel")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(308, 171, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:4px")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(308, 292, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:4px")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.adresseLabel = QtWidgets.QLabel(Form)
        self.adresseLabel.setGeometry(QtCore.QRect(127, 292, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.adresseLabel.setFont(font)
        self.adresseLabel.setStyleSheet("color:rgb(70,68,68)")
        self.adresseLabel.setObjectName("adresseLabel")

        self.emailLabel = QtWidgets.QLabel(Form)
        self.emailLabel.setGeometry(QtCore.QRect(127, 353, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.emailLabel.setFont(font)
        self.emailLabel.setStyleSheet("color:rgb(70,68,68)")
        self.emailLabel.setObjectName("emailLabel")

        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(308, 353, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius:4px")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 421, 151, 32))
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
        self.pushButton_2.setGeometry(QtCore.QRect(390, 421, 151, 32))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "         Ajouter Un Gestionnaire"))
        self.nomLabel.setText(_translate("Form", "Nom Complet:"))
        self.TeleLabel.setText(_translate("Form", "Telephone:"))
        self.idLabel.setText(_translate("Form", "ID:"))
        self.adresseLabel.setText(_translate("Form", "Adresse:"))
        self.emailLabel.setText(_translate("Form", "Email:"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.pushButton_2.setText(_translate("Form", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())

