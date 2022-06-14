from PyQt5 import QtCore, QtGui, QtWidgets
from Data import *
from PyQt5.QtWidgets import *


def loaddata(self):
    serviceList = get_allservice()
    row = 0
    self.tableWidget.setRowCount(len(serviceList))
    for service in serviceList:
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(service.iD))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(service.nom))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(service.gestionnaire.nom_complet))
        row += 1


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def validate(self):
    gest = get_gestionnaire(Ui_Form.gest_id)
    try:
        if gest.id == "0000":
            item = self.tableWidget.currentItem()
            if item is not None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                # setting message for Message Box
                msg.setText("Le service a été affecter avec succès à l'admin")

                # setting Message box window title
                msg.setWindowTitle("Opération réussie")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
                row = self.tableWidget.currentRow()
                service = get_service(self.tableWidget.item(row, 0).text())
                service.set_gestionnaire(gest)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Aucun service sélectionné. Veuillez d'abord sélectionner un service.")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
        else:
            item = self.tableWidget.currentItem()
            if item is not None:
                row = self.tableWidget.currentRow()
                serviceid = self.tableWidget.item(row, 0).text()
                if serviceid != "00":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)

                    # setting message for Message Box
                    msg.setText("Le service a été affecter avec succès à "+gest.nom_complet)

                    # setting Message box window title
                    msg.setWindowTitle("Opération réussie")

                    # declaring buttons on Message Box
                    msg.setStandardButtons(QMessageBox.Ok)

                    # start the app
                    retval = msg.exec_()
                    service = get_service(serviceid)
                    service.set_gestionnaire(gest)
                else:  # we can't assign default service to other managers than admin
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)

                    # setting message for Message Box
                    msg.setText("""Impossible d'affecter le service par défaut à un gestionnaire autre que l'admin.
                                Veuillez sélectionner un autre service.""")

                    # setting Message box window title
                    msg.setWindowTitle("Opération échouée")

                    # declaring buttons on Message Box
                    msg.setStandardButtons(QMessageBox.Ok)

                    # start the app
                    retval = msg.exec_()
            else:  # no service selected
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Aucun service sélectionné. Veuillez sélectionner d'abord un service.")

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
    previouswidth = "index"
    widget = ""
    previousindex = ""
    gest_id = ""

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        loaddata(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 424)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 751, 51))
        self.label_2.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 50, 751, 401))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 10, 111, 32))
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
        self.pushButton_2.setGeometry(QtCore.QRect(600, 120, 141, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: validate(self))

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 61, 581, 351))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 116)
        self.tableWidget.setColumnWidth(1, 232)
        self.tableWidget.setColumnWidth(2, 233)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_8.setText(_translate("Form", "Retour"))
        self.pushButton_2.setText(_translate("Form", "Valider"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Service"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nom Gestionnaire"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.Form.show()
    sys.exit(app.exec_())
