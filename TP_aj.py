import csv

def ajouter_commande(id_client, id_produit,quantite,total):
    with open("TPCSV3.csv", "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id_client","id_produit","quantite","total"], delimiter=";")
        writer.writerow({
            "id_client": id_client,
            "id_produit": id_produit,
            "quantite": quantite,
            "total": total
        })
ajouter_commande(2,3,1,24)