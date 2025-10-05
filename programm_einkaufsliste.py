# Artikel hinzufügen
# Akton hinzufügen, entfernen, anzeigen, beenden

lebensmittelliste = []
entscheidung = "y"
while entscheidung == "y":
    lebensmittelliste.append(input("Was möchtest du deiner Liste hinzufügen? "))
    entscheidung = (input("Möchtest du weitere Artikel hinzufügen ? (y / n)"))
print(lebensmittelliste)

lebensmittelliste.pop(input("Was möchtest du löschen: "))
print(lebensmittelliste)