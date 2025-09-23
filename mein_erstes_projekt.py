x = input("Wie ist dein Name?")
print("Dein Name lautet: " + x)
# int muss vor dem input benutzen, da wir eine Ganzzahl erwarten,
# ansonsten wird einen Fehler in der Konsole ausgegeben.
y = int(input("Wie viel ist dein Ausgangsgehalt: ?"))

z = y * 1.10
print(z)

print()
# Erstelle ein Projekt, indem du eine Eingabe einführst und dann
# am Ende eine Ausgabe in einer anderen Währung
eingabe_euro = float(input("Wie viel Euro hast du? "))
cuc = eingabe_euro * 30.05
print("Super! Deine ", eingabe_euro, "Euro sind ", cuc, "cuc wert.")

