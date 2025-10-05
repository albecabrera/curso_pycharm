
einkaufsliste = []
entscheidung = "y"

while entscheidung == "y":
    einkaufsliste.append(input("Was möchtest du deiner Liste hinzufügen? "))
    entscheidung = (input("Möchtest du weitere Artikel hinzufügen ? (y / n)"))
print(einkaufsliste)