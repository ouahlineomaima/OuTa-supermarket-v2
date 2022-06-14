from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Data import *


def loaddata(self):
    gest = get_gestionnaire(Ui_Form.gestid)
    self.adresseLabel.setText(gest.address)
    self.teleLabel.setText(gest.telephone)
    self.passLabel.setText("*"*10)
    self.emailLabel.setText(gest.email)
    self.idlabel.setText(Ui_Form.gestid)
    self.nomLabel.setText(gest.nom_complet)


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def validate(self):
    try:
        path = self.pathtextfield.text()
        x = "aaa\ aaa"
        Ui_Form.picpath = path.replace(x[3]+x[3], "/")
        file = open(path)
        Ui_Form.goodpath = True
        Ui_Form.validatepressed = True
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("l'image a été changée avec succès.")

        # setting Message box window title
        msg.setWindowTitle("Opération réussie")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()
        return
    except FileNotFoundError as e:
        Ui_Form.goodpath = False
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("Veuillez saisir un chemin valide.")

        # setting Message box window title
        msg.setWindowTitle("Opération échouée")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()
        print(e)
    except BaseException as e:
        print(e)


class Ui_Form(object):
    widget = ""
    previousheight = ""
    previouswidth = ""
    previousindex = ""
    loginwidth = ""
    loginheight = ""
    gestid = ""
    picpath = ""
    goodpath = False
    validatepressed = False

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
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
        self.label_2.setGeometry(QtCore.QRect(0, 0, 751, 51))
        self.label_2.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(0, 0, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "background-color:rgb(13,12,60)")
        self.label_20.setObjectName("label_20")

        self.imageLabel = QtWidgets.QLabel(Form)
        self.imageLabel.setGeometry(QtCore.QRect(40, 80, 111, 111))
        self.imageLabel.setAutoFillBackground(False)
        self.imageLabel.setStyleSheet("border-radius:40px")
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QtGui.QPixmap(Ui_Form.picpath))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")

        self.pathtextfield = QtWidgets.QLineEdit(Form)
        self.pathtextfield.setGeometry(QtCore.QRect(15, 220, 175, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pathtextfield.setFont(font)
        self.pathtextfield.setStyleSheet("border-radius:4px")
        self.pathtextfield.setObjectName("pathtextfield")

        self.labeltxt = QtWidgets.QLabel(Form)
        self.labeltxt.setGeometry(QtCore.QRect(20, 250, 165, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labeltxt.setFont(font)
        self.labeltxt.setObjectName("labeltxt")

        self.validerpicbtn = QtWidgets.QPushButton(Form)
        self.validerpicbtn.setGeometry(QtCore.QRect(130, 190, 26, 26))
        self.validerpicbtn.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.validerpicbtn.setText("")
        self.validerpicbtn.setObjectName("validerpicbtn")
        self.validerpicbtn.setIcon(QIcon("validate.png"))
        self.validerpicbtn.setIconSize(QSize(26, 26))
        self.validerpicbtn.clicked.connect(lambda: validate(self))

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.idlabel = QtWidgets.QLabel(Form)
        self.idlabel.setGeometry(QtCore.QRect(370, 120, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idlabel.setFont(font)
        self.idlabel.setObjectName("idlabel")

        self.nomLabel = QtWidgets.QLabel(Form)
        self.nomLabel.setGeometry(QtCore.QRect(370, 160, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nomLabel.setFont(font)
        self.nomLabel.setObjectName("nomLabel")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(370, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(370, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(200, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(200, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(200, 280, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(200, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.adresseLabel = QtWidgets.QLabel(Form)
        self.adresseLabel.setGeometry(QtCore.QRect(370, 240, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.adresseLabel.setFont(font)
        self.adresseLabel.setObjectName("adresseLabel")

        self.teleLabel = QtWidgets.QLabel(Form)
        self.teleLabel.setGeometry(QtCore.QRect(370, 200, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.teleLabel.setFont(font)
        self.teleLabel.setObjectName("teleLabel")

        self.passLabel = QtWidgets.QLabel(Form)
        self.passLabel.setGeometry(QtCore.QRect(370, 320, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passLabel.setFont(font)
        self.passLabel.setObjectName("passLabel")

        self.emailLabel = QtWidgets.QLabel(Form)
        self.emailLabel.setGeometry(QtCore.QRect(370, 280, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 380, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.clicked.connect(lambda: go_back())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_20.setText(_translate("Form", "          Profil"))
        self.label_3.setText(_translate("Form", "Id Gestionnaire:"))
        self.idlabel.setText(_translate("Form", "1"))
        self.nomLabel.setText(_translate("Form", "Omaima ouahline"))
        self.label_6.setText(_translate("Form", "Nom Complet:"))
        self.label_9.setText(_translate("Form", "Adresse:"))
        self.label_10.setText(_translate("Form", "Téléphone:"))
        self.label_11.setText(_translate("Form", "E-mail:"))
        self.label_12.setText(_translate("Form", "Password:"))
        self.labeltxt.setText(_translate("Form", """Veuillez saisir le chemin 
    absolu de l'image"""))
        self.adresseLabel.setText(_translate("Form", "rabat"))
        self.teleLabel.setText(_translate("Form", "06 12 20 27 83"))
        self.passLabel.setText(_translate("Form", "**************"))
        self.emailLabel.setText(_translate("Form", "nom@gmail.com"))
        self.pushButton_3.setText(_translate("Form", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())
