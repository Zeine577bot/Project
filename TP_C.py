import csv
def ajouter_client(id,nom,age):
    with open("TP_CSV2.csv","a", newline="")as f:
        writer = csv.DictWriter(f, fieldnames=["id","nom","age"], delimiter=";")
        writer.writerow({"id":id,"nom":nom,"age":age})
ajouter_client(3,"sara",22)