import mysql.connector


def get_connection():
    db = mysql.connector.connect(host="localhost", user="root",
                                 passwd="root", database="gestionstock")
    return db.cursor(), db


class Service:

    def __init__(self, iD, nom, gestionnaire):
        self.iD = iD
        self.nom = nom
        self.gestionnaire = gestionnaire

    def set_gestionnaire(self, gestionnaire):
        self.gestionnaire = gestionnaire
        cursor, db = get_connection()
        cursor.execute(f"UPDATE `gestionstock`.`service` SET `idgestionnaire` = '{gestionnaire.id}' WHERE (`idservice` = '{self.iD}')")
        db.commit()
        return cursor.rowcount

    def __str__(self):
        return self.nom

    def __hash__(self):
        return hash(self.iD)
