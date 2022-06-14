import mysql.connector
from Produit import Produit
from Gestionnaire import Gestionnaire
from Admin import Admin
from Service import Service


def get_connection():
    db = mysql.connector.connect(host="localhost", user="root",
                                 passwd="root", database="gestionstock")
    return db.cursor(), db


def get_allgestionnaire():
    list_gestionnaire = []
    try:
        cursor, db = get_connection()
        request = "SELECT idgestionnaire, nomComplet, telephone, address, email, password FROM gestionnaire"
        cursor.execute(request)
        row = cursor.fetchone()
        while row is not None:
            id, nom, tele, address, email, passwd = row
            if id == "0000":
                admin = Admin(nom, id, email, address, tele, passwd)
                list_gestionnaire.append(admin)
            else:
                gest = Gestionnaire(nom, id, email, address, tele, passwd)
                list_gestionnaire.append(gest)
            row = cursor.fetchone()
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
        row = cursor.fetchone()
        while row is not None:
            id, nom, id_gest = row
            gestionnaire = get_gestionnaire(id_gest)
            for gest in get_allgestionnaire():
                if gest.id == id_gest:
                    gestionnaire = gest
            service = Service(id, nom, gestionnaire)
            list_service.append(service)
            row = cursor.fetchone()
        return list_service
    except mysql.connector.Error:
        return list_service


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
        cursor.close()
        return list_produit
    except mysql.connector.Error as e:
        print(e)
        return list_produit


def get_gest_services(id_gest):
    cursor, db = get_connection()
    request = f"SELECT * FROM service WHERE idgestionnaire = {id_gest}"
    cursor.execute(request)
    servicelist = []
    row = cursor.fetchone()
    while row is not None:
        id, nom, _ = row
        gest = get_gestionnaire(id_gest)
        service = Service(id, nom, gest)
        servicelist.append(service)
        row = cursor.fetchone()
    cursor.close()
    return servicelist


def get_gestionnaire(id_gest):
    for gest in get_allgestionnaire():
        if gest.id == id_gest:
            return gest
    return None


def get_gestionnaire_by_name(gest_name):
    for gest in get_allgestionnaire():
        if gest_name == gest.nom_complet:
            return gest
    return None


def get_service(id_service):
    for service in get_allservice():
        if service.iD == id_service:
            return service
    return None


def get_produit(id_produit, service):
    try:
        for produit in get_allproduit(service):
            if produit.iD == id_produit:
                return produit
        return None
    except BaseException as e:
        print(e)


def add_produit(produit, service):
    x = 0
    for s in get_allservice():
        if get_produit(produit.iD, s) is not None:
            x = 1
            break
    if x == 0:
        try:
            cursor, db = get_connection()
            request = f"""INSERT INTO `gestionstock`.`produit` (`idproduit`, `nom`, `quantite`, `service`, `prix`, `min`, `max`) VALUES ('{produit.iD}', '{produit.nom}', '{produit.quantite}', '{produit.service.iD}', '{produit.prix}', '{produit.min}', '{produit.max}');"""
            cursor.execute(request)
            db.commit()
            return cursor.rowcount
        except mysql.connector.Error as e:
            print(e)
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
    except mysql.connector.Error as e:
        print(e)
        return -1


def modify_produit(new_produit, old_produit):
    try:
        delete_produit(old_produit.iD)
        add_produit(new_produit, old_produit.service)
        return 1
    except mysql.connector.Error:
        return -1


def ajouter_service(service):
    cursor, db = get_connection()
    request = "INSERT INTO service VALUES (%s, %s, %s)"
    val = (service.iD, service.nom, service.gestionnaire.id)
    cursor.execute(request, val)
    db.commit()
    return cursor.rowcount


def affecter_service(gestionnaire, service):
    return service.set_gestionnaire(gestionnaire)


def supprimer_gestionnaire(gestionnaire):
    cursor, db = get_connection()
    request = "DEELET FROM gestionnaire WHERE idgestionnaire = %s"
    val = gestionnaire.id
    cursor.execute(request, val)
    db.commit()
    return cursor.rowcount


def supprimer_service(serviceid):
    try:
        cursor, db = get_connection()
        request = f"DELETE FROM `gestionstock`.`service` WHERE (`idservice` = '{serviceid}')"
        cursor.execute(request)
        db.commit()
        return cursor.rowcount
    except mysql.connector.Error as e:
        return 0


def commit_commande(commande):
    try:
        cursor, db = get_connection()
        req = f"INSERT INTO `gestionstock`.`commande` (`idcommande`) VALUES ('{commande.iD}')"
        cursor.execute(req)
        db.commit()
        cursor.close()
        productss = commande.produit.keys()
        products = list(productss)
        qty = commande.produit.values()
        qt = list(qty)
        for i in range(len(products)):
            req = f"INSERT INTO `gestionstock`.`acheter` (`idproduit`, `idcommande`, `quantite`, `prix`, `total`) VALUES ('{products[i].iD[6:]}', '{commande.iD}', '{qt[i]}', '{products[i].prix}', '{qt[i]*products[i].prix}')"
            cursor, db = get_connection()
            cursor.execute(req)
            db.commit()
            cursor.close()
    except BaseException as e:
        print(e)


def get_last_commande_id():
    try:
        cursor, db = get_connection()
        req = "SELECT * FROM gestionstock.commande ORDER BY idcommande DESC"
        cursor.execute(req)
        row = cursor.fetchone()
        if not row:
            id = 0
        else:
            id, = row
        return id
    except BaseException as e:
        print(e)










