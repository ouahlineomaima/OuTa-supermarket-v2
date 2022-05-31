from Data import *


class Produit:

    def __init__(self, iD, nom, quantite, min, max, service, prix):
        self.iD = iD
        self.nom = nom
        self.quantite = quantite
        self.min = min
        self.max = max
        self.service = service
        self.prix = prix

    def set_service(self, service):
        self.service = service
        cursor, db = get_connection()
        cursor.execute(f"update produit set service = {self.service.iD} where idproduit = {self.iD}")

    def achat_produit(self, quantite):
        product = get_produit(self.iD[6:])
        product.quantite -= quantite
        cursor, db = get_connection()
        cursor.execute(f"update produit set quantite = {product.quantite} where idproduit = {product.iD}")
