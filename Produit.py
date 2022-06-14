import mysql.connector
from PyQt5.QtWidgets import *
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


def get_connection():
    db = mysql.connector.connect(host="localhost", user="root",
                                 passwd="root", database="gestionstock")
    return db.cursor(), db


def get_allproduit(service):
    list_produit = []
    try:
        cursor, db = get_connection()
        request = f"SELECT * FROM produit WHERE service = {service.iD}"
        cursor.execute(request)
        row = cursor.fetchone()
        while row is not None:
            id, nom, quantite, _, prix, mini, maxi = row
            produit = Produit(id, nom, int(quantite), int(mini), int(maxi), service, int(prix))
            list_produit.append(produit)
            row = cursor.fetchone()
        return list_produit
    except mysql.connector.Error:
        return list_produit


def get_produit(id_produit, service):
    for produit in get_allproduit(service):
        if produit.iD == id_produit:
            return produit
    return None


class Produit:

    def __init__(self, iD, nom, quantite, min, max, service, prix):
        try:
            self.iD = iD
            self.nom = nom
            self.quantite = int(quantite)
            if not min:
                self.min = 0
            else:
                self.min = int(min)
            if not max:
                self.max = 100
            else:
                self.max = int(max)
            self.service = service
            try:
                self.prix = float(prix)
            except TypeError as e:
                print(e)
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
        except BaseException as e:
            print(e)

    def set_service(self, service):
        try:
            self.service = service
            cursor, db = get_connection()
            cursor.execute(f"UPDATE `gestionstock`.`produit` SET `service` = '{service.iD}' WHERE (`idproduit` = '{self.iD}');")
            db.commit()
        except mysql.connector.Error as e:
            print(e.msg)

    def achat_produit(self, quantite):
        try:
            product = get_produit(self.iD[6:], self.service)
            product.quantite -= quantite
            if product.quantite - 5 < product.min:
                service = product.service
                gest = service.gestionnaire
                destination = gest.email
                nom = product.nom
                message = f"""le stock disponible du produit {nom} dans le service {service} est proche du minimum. 
Veuillez ajouter ce produit."""
                send_email(message, destination)
            cursor, db = get_connection()
            cursor.execute(f"UPDATE `gestionstock`.`produit` SET `quantite` = '{product.quantite}' WHERE (`idproduit` = '{product.iD}')")
            db.commit()
            cursor.close()
        except BaseException as e:
            print(e)

    def __str__(self):
        return self.nom

    def __eq__(self, other):
        if isinstance(other, Produit):
            return self.iD == other.iD and self.nom == other.nom and self.quantite == other.quantite and self.min == other.min and self.max == other.max and self.service.iD == other.service.iD and self.prix == other.prix
        return False

    def __hash__(self):
        return hash(self.iD)
