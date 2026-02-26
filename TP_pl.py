import csv

def produit_plus_commande():
    d = {}

    with open("TPCSV3.csv","r") as f:
        reader = csv.DictReader(f, delimiter=";")
        for ligne in reader:
            id_p = ligne["id_produit"]
            qte = int(ligne["quantite"])
            d[id_p] = d.get(id_p, 0) + qte
    return max(d, key=d.get)
print("produit plus commande : " , produit_plus_commande())