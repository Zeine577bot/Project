import csv

def chiffre_affaire():
    total=0

    with open ("TPCSV3.csv","r") as f:
        reader= csv.DictReader(f, delimiter=";")
        for ligne in reader:
            total+= int(ligne["total"])
    return total
print("chaiffre affire :", chiffre_affaire())