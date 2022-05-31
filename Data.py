import mysql.connector
from Produit import Produit
from Gestionnaire import Gestionnaire
from Admin import Admin
from Service import Service
# test commit and push


def get_connection():
    db = mysql.connector.connect(host="localhost", user="root",
                                 passwd="root", database="gestionstock")
    return db.cursor(), db


def get_allgestionnaire():
    list_gestionnaire = []
    try:
        cursor, db = get_connection()
        request = "SELECT * FROM gestionnaire"
        cursor.execute(request)
        while cursor.fetchone() is not None:
            id, nom, tele, address, email, passwd = cursor.fetchone()
            if id == "0000":
                admin = Admin(nom, id, email, address, tele)
                list_gestionnaire.append(admin)
            else:
                gest = Gestionnaire(nom, id, email, address, tele)
                list_gestionnaire.append(gest)
        cursor.close()
        return list_gestionnaire
    except mysql.connector.Error:
        return list_gestionnaire


def get_allservice():
    list_service = []
    try:
        cursor, db = get_connection()
        request = "SELECT * FROM service"
        cursor.execute(request)
        while cursor.fetchone() is not None:
            id, nom, id_gest = cursor.fetchone()
            gestionnaire = Gestionnaire()
            for gest in get_allgestionnaire():
                if gest.id == id_gest:
                    gestionnaire = gest
            service = Service(id, nom, gestionnaire)
            list_service.append(service)
        return list_service
    except mysql.connector.Error:
        return list_service


def get_allproduit(service):
    list_produit = []
    try:
        cursor, db = get_connection()
        request = f"SELECT * FROM produit WHERE service = {service.iD}"
        cursor.execute(request)
        while cursor.fetchone() is not None:
            id, nom, quantite, _, prix, mini, maxi = cursor.fetchone()
            produit = Produit(id, nom, int(quantite), int(mini), int(maxi), service, int(prix))
            list_produit.append(produit)
        return list_produit
    except mysql.connector.Error:
        return list_produit


def get_gestionnaire(id_gest):
    for gest in get_allgestionnaire():
        if gest.id == id_gest:
            return gest
    return None


def get_service(id_service):
    for service in get_allservice():
        if service.iD == id_service:
            return service
    return None


def get_produit(id_produit, service):
    for produit in get_allproduit(service):
        if produit.iD == id_produit:
            return produit
    return None


def add_produit(produit, service):
    x = 0
    for s in get_allservice():
        if get_produit(produit.iD, s) is not None:
            x = 1
            break
    if x == 0:
        try:
            cursor, db = get_connection()
            request = f"""INSERT INTO produit VALUES ({produit.iD}, {produit.nom}, 
                    {produit.quantite}, f{produit.service.iD}, {produit.prix},
                    {produit.min}, {produit.max})"""
            cursor.execute(request)
            db.commit()
            return cursor.rowcount
        except mysql.connector.Error:
            return -1
    else:
        return -2


def delete_produit(idproduit):
    try:
        cursor, db = get_connection()
        request = f"DELETE FROM produit WHERE idproduit = {idproduit}"
        cursor.execute(request)
        db.commit()
        return cursor.rowcount
    except mysql.connector.Error:
        return -1


def modify_produit(new_produit, old_produit):
    try:
        delete_produit(old_produit)
        add_produit(new_produit, old_produit.service)
        return 1
    except mysql.connector.Error:
        return -1








