# test commit and push


class Gestionnaire:

    def __init__(self, nom_complet, iD, email, address, telephone, passwd):
        self.nom_complet = nom_complet
        self.id = iD
        self.email = email
        self.address = address
        self.telephone = telephone
        self.password = passwd

    def __str__(self):
        return self.nom_complet