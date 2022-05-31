from Data import *


class Service:

    def __init__(self, iD, nom, gestionnaire):
        self.iD = iD
        self.nom = nom
        self.gestionnaire = gestionnaire

    def set_gestionnaire(self, gestionnaire):
        self.gestionnaire = gestionnaire
        cursor, db = get_connection()
        cursor.execute(f"update service set idgestionnaire = {gestionnaire.id} where idservice = {self.iD}")
        return cursor.rowcount()

    def __str__(self):
        return self.nom