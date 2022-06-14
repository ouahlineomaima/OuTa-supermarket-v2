from PyQt5 import QtCore, QtGui, QtWidgets
from Data import *
import hashlib
import sys
from PyQt5.QtWidgets import *
import TableService
import affichageGestionnaire


class Ui_Form(object):
    admin_first = False
    gest_first = False
    admin_index = 0
    gest_index = 0

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        self.gest = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 491)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 451, 491))
        self.label_2.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(450, 0, 301, 491))
        self.label_3.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(54, 54, 54)")
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 130, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(70,68,68)")
        self.label_4.setObjectName("label_4")

        self.idfield = QtWidgets.QLineEdit(Form)
        self.idfield.setGeometry(QtCore.QRect(170, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.idfield.setFont(font)
        self.idfield.setStyleSheet("border-radius:4px")
        self.idfield.setObjectName("idfield")

        self.nomfield = QtWidgets.QLineEdit(Form)
        self.nomfield.setGeometry(QtCore.QRect(170, 190, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nomfield.setFont(font)
        self.nomfield.setStyleSheet("border-radius:4px")
        self.nomfield.setObjectName("nomfield")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(70,68,68)")
        self.label_5.setObjectName("label_5")

        self.passwordfield = QtWidgets.QLineEdit(Form)
        self.passwordfield.setGeometry(QtCore.QRect(170, 260, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.passwordfield.setFont(font)
        self.passwordfield.setStyleSheet("border-radius:4px")
        self.passwordfield.setObjectName("passwordfield")
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(70,68,68)")
        self.label_6.setObjectName("label_6")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 350, 191, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                      " color:rgb(255, 255, 255);\n"
                                      "border-radius:4px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sign_in)

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(570, 240, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(85, 255, 0);")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(540, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(255,255,255)")
        self.label_9.setObjectName("label_9")

        self.imageLabel = QtWidgets.QLabel(Form)
        self.imageLabel.setGeometry(QtCore.QRect(520, 90, 161, 141))
        self.imageLabel.setAutoFillBackground(False)
        self.imageLabel.setStyleSheet("border-radius:40px")
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QtGui.QPixmap("logo.png"))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")

        self.id = self.idfield.text()
        self.nom = self.nomfield.text()
        self.passwd = self.passwordfield.text()
        self.gest = get_gestionnaire(self.id)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def sign_in(self):
        try:
            self.id = self.idfield.text()
            self.nom = self.nomfield.text()
            self.passwd = self.passwordfield.text()
            self.gest = get_gestionnaire(self.id)
            if self.gest is not None:
                if self.nom == self.gest.nom_complet:
                    if hashlib.md5(self.passwd.encode()).hexdigest() == self.gest.password:
                        if self.id == "0000":  # admin part
                            self.idfield.setText("")
                            self.nomfield.setText("")
                            self.passwordfield.setText("")
                            TableService.Ui_Form.widget = widget
                            TableService.Ui_Form.loginheight = loginui.Form.frameGeometry().height()
                            TableService.Ui_Form.loginwidth = loginui.Form.frameGeometry().width()
                            adminui = TableService.Ui_Form()
                            widget.addWidget(adminui.Form)
                            if not Ui_Form.admin_first and not Ui_Form.gest_first:
                                Ui_Form.admin_first = True
                                Ui_Form.admin_index = 1
                                Ui_Form.gest_index = 2

                                defaultpass = self.id + self.nom
                                if hashlib.md5(defaultpass.encode()).hexdigest() == self.gest.password:
                                    msg = QMessageBox()
                                    msg.setIcon(QMessageBox.Warning)

                                    # setting message for Message Box
                                    msg.setText("Veuillez changer votre mot de pass par défaut dans la partie profil.")

                                    # setting Message box window title
                                    msg.setWindowTitle("Avertissement")

                                    # declaring buttons on Message Box
                                    msg.setStandardButtons(QMessageBox.Ok)

                                    # start the app
                                    retval = msg.exec_()

                                    widget.setFixedWidth(adminui.Form.frameGeometry().width())
                                    widget.setFixedHeight(adminui.Form.frameGeometry().height())
                                    widget.setCurrentIndex(Ui_Form.admin_index)
                                else:
                                    widget.setFixedWidth(adminui.Form.frameGeometry().width())
                                    widget.setFixedHeight(adminui.Form.frameGeometry().height())
                                    widget.setCurrentIndex(Ui_Form.admin_index)

                            else:
                                defaultpass = self.id + self.nom
                                if hashlib.md5(defaultpass.encode()).hexdigest() == self.gest.password:
                                    msg = QMessageBox()
                                    msg.setIcon(QMessageBox.Warning)

                                    # setting message for Message Box
                                    msg.setText("Veuillez changer votre mot de pass par défaut dans la partie profil.")

                                    # setting Message box window title
                                    msg.setWindowTitle("Avertissement")

                                    # declaring buttons on Message Box
                                    msg.setStandardButtons(QMessageBox.Ok)

                                    # start the app
                                    retval = msg.exec_()

                                    widget.setFixedWidth(adminui.Form.frameGeometry().width())
                                    widget.setFixedHeight(adminui.Form.frameGeometry().height())
                                    widget.setCurrentIndex(Ui_Form.admin_index)
                                else:
                                    widget.setFixedWidth(adminui.Form.frameGeometry().width())
                                    widget.setFixedHeight(adminui.Form.frameGeometry().height())
                                    widget.setCurrentIndex(Ui_Form.admin_index)
                                widget.setFixedWidth(adminui.Form.frameGeometry().width())
                                widget.setFixedHeight(adminui.Form.frameGeometry().height())
                                widget.setCurrentIndex(Ui_Form.admin_index)

                        else:  # normal gest part
                            self.idfield.setText("")
                            self.nomfield.setText("")
                            self.passwordfield.setText("")
                            affichageGestionnaire.Ui_Form.gest_id = self.id
                            affichageGestionnaire.Ui_Form.widget = widget
                            affichageGestionnaire.Ui_Form.loginheight = loginui.Form.frameGeometry().height()
                            affichageGestionnaire.Ui_Form.loginwidth = loginui.Form.frameGeometry().width()
                            gestui = affichageGestionnaire.Ui_Form()
                            widget.addWidget(gestui.Form)
                            if not Ui_Form.admin_first and not Ui_Form.gest_first:
                                Ui_Form.gest_first = True
                                Ui_Form.gest_index = 1
                                Ui_Form.admin_index = 2

                                defaultpass = self.id + self.nom
                                if hashlib.md5(defaultpass.encode()).hexdigest() == self.gest.password:
                                    msg = QMessageBox()
                                    msg.setIcon(QMessageBox.Warning)

                                    # setting message for Message Box
                                    msg.setText("Veuillez changer votre mot de pass par défaut dans la partie profil.")

                                    # setting Message box window title
                                    msg.setWindowTitle("Avertissement")

                                    # declaring buttons on Message Box
                                    msg.setStandardButtons(QMessageBox.Ok)

                                    # start the app
                                    retval = msg.exec_()

                                    widget.setFixedWidth(gestui.Form.frameGeometry().width())
                                    widget.setFixedHeight(gestui.Form.frameGeometry().height())
                                    widget.setCurrentIndex(Ui_Form.gest_index)
                            else:
                                defaultpass = self.id + self.nom
                                if hashlib.md5(defaultpass.encode()).hexdigest() == self.gest.password:
                                    msg = QMessageBox()
                                    msg.setIcon(QMessageBox.Warning)

                                    # setting message for Message Box
                                    msg.setText("Veuillez changer votre mot de pass par défaut dans la partie profil.")

                                    # setting Message box window title
                                    msg.setWindowTitle("Avertissement")

                                    # declaring buttons on Message Box
                                    msg.setStandardButtons(QMessageBox.Ok)

                                    # start the app
                                    retval = msg.exec_()
                                    widget.setFixedWidth(gestui.Form.frameGeometry().width())
                                    widget.setFixedHeight(gestui.Form.frameGeometry().height())
                                    widget.setCurrentIndex(Ui_Form.gest_index)

                    else:  # wrong passwd
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)

                        # setting message for Message Box
                        msg.setText("Mot de pass incorrect")

                        # setting Message box window title
                        msg.setWindowTitle("Opération échouée")

                        # declaring buttons on Message Box
                        msg.setStandardButtons(QMessageBox.Ok)

                        # start the app
                        retval = msg.exec_()
                else:  # wrong name
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)

                    # setting message for Message Box
                    msg.setText("Nom incorrect")

                    # setting Message box window title
                    msg.setWindowTitle("Opération échouée")

                    # declaring buttons on Message Box
                    msg.setStandardButtons(QMessageBox.Ok)

                    # start the app
                    retval = msg.exec_()
            else:  # wrong information
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Aucun gestionnaire ne correspond à l'id saisi")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
        except BaseException as e:
            print(e)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Authentification"))
        self.label_4.setText(_translate("Form", "ID:"))
        self.label_5.setText(_translate("Form", "Nom Complet:"))
        self.label_6.setText(_translate("Form", "Mot de Passe:"))
        self.pushButton.setText(_translate("Form", "Se Connecter "))
        self.label_8.setText(_translate("Form", "Ou&Ta"))
        self.label_9.setText(_translate("Form", "Supermarket"))

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

loginui = Ui_Form()
loginui.setupUi(loginui.Form)
widget.addWidget(loginui.Form)


widget.setFixedWidth(loginui.Form.frameGeometry().width())
widget.setFixedHeight(loginui.Form.frameGeometry().height())

widget.show()
sys.exit(app.exec_())
