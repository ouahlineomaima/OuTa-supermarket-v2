from Gestionnaire import Gestionnaire
import mysql.connector


def get_connection():
    db = mysql.connector.connect(host="localhost", user="root",
                                 passwd="root", database="gestionstock")
    return db.cursor(), db


class Admin(Gestionnaire):

    def ajouter_service(self, service):
        cursor, db = get_connection()
        request = "INSERT INTO service VALUES (%s, %s, %s)"
        val = (service.iD, service.nom, service.gestionnaire.id)
        cursor.execute(request, val)
        db.commit()
        return cursor.rowcount

    def ajouter_gestionnaire(self, gestionnaire_iD, gestionnaire_nom_complet, gestionnaire_telephone, gestionnaire_address, gestionnaire_email, gestionnaire_password, path="profil1.png"):
        cursor, db = get_connection()
        request = "INSERT INTO gestionnaire VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (gestionnaire_iD, gestionnaire_nom_complet, gestionnaire_telephone, gestionnaire_address, gestionnaire_email, gestionnaire_password, path)
        cursor.execute(request, val)
        db.commit()
        return cursor.rowcount

    def affecter_service(self, gestionnaire, service):
        return service.set_gestionnaire(gestionnaire)

    def supprimer_gestionnaire(self, gestionnaire_id):
        cursor, db = get_connection()
        request = f"DELETE FROM `gestionstock`.`gestionnaire` WHERE (`idgestionnaire` = '{gestionnaire_id}')"
        cursor.execute(request)
        db.commit()
        return cursor.rowcount

    def supprimer_service(self, serviceid):
        try:
            cursor, db = get_connection()
            request = f"DELETE FROM `gestionstock`.`service` WHERE (`idservice` = '{serviceid}')"
            cursor.execute(request)
            db.commit()
            return cursor.rowcount
        except mysql.connector.Error as e:
            return 0
