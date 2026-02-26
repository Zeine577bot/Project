import csv

def produit_plus_cher():
    max_prix= 0
    produit =None

    with open("TPCSV1.csv","r")as f:
        reader = csv.DictReader(f, delimiter=";")
        for ligne in reader:
            prix = int(ligne["prix"])
            if prix > max_prix:
                max_prix = prix
                produit = ligne
    return produit
print("produit plus cher : " , produit_plus_cher())