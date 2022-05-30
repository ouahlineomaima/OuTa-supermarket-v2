from Gestionnaire import Gestionnaire
from Data import get_connection


class Admin(Gestionnaire):
    def ajouter_service(self, service):
        cursor, db = get_connection()
        request = "INSERT INTO service VALUES (%s, %s, %s)"
        val = (service.iD, service.nom, service.gestionnaire.id)
        cursor.execute(request, val)
        db.commit()
        return cursor.rowcount()

    def ajouter_gestionnaire(self, gestionnaire):
        cursor, db = get_connection()
        request = "INSERT INTO gestionnaire VALUES (%s, %s, %s, %s, %s, %s)"
        val = (gestionnaire.iD, gestionnaire.nom_complet, gestionnaire.telephone, gestionnaire.address, gestionnaire.email, gestionnaire.password)
        cursor.execute(request, val)
        db.commit()
        return cursor.rowcount()

    def affecter_service(self, gestionnaire, service):
        return service.set_gestionnaire(gestionnaire)

    def supprimer_gestionnaire(self, gestionnaire):
        cursor, db = get_connection()
        request = "DEELET FROM gestionnaire WHERE idgestionnaire = %s"
        val = gestionnaire.id
        cursor.execute(request, val)
        db.commit()
        return cursor.rowcount

    def supprimer_service(self, service):
        cursor, db = get_connection()
        request = "DEELET FROM gestionnaire WHERE idgestionnaire = %s"
        val = service.id
        cursor.execute(request, val)
        db.commit()
        return cursor.rowcount