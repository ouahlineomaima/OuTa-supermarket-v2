class Commande:

    def __init__(self, iD, produit):
        self.iD = iD
        self.produit = produit

    def achat_produit(self):
        try:
            product = self.produit
            produitss = product.keys()
            produits = list(produitss)
            quantitess = product.values()
            quantites = list(quantitess)
            for i in range(len(produits)):
                produits[i].achat_produit(quantites[i])
        except BaseException as e:
            print(e)

    def __hash__(self):
        return hash(self.iD)

