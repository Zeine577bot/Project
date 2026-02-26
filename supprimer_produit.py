import csv

def supprimer_produit(id_produit):
    lignes = []
    with open("TPCSV1.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        for ligne in reader:
            if ligne["id"] != str(id_produit):
                lignes.append(ligne)
    with open("TPCSV1.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id","nom","quantite","prix"],
            delimiter=";"
        )
        writer.writeheader()
        writer.writerows(lignes)
supprimer_produit(2)