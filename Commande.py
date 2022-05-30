class Commande:

    def __init__(self, iD, produit):
        self.iD = iD
        self.produit = produit

    def achat_produit(self, product):
        produits = product.Keys()
        quantites = product.Values()
        for i in range(len(produits)):
            produits[i].achat_produit(quantites[i])