#  Printbefehle
# print("Hallo Welt!")
# print()
# print("Hallo", "Welt", "!")
# print()
# print("Hallo" + "Welt" + "!")
# print()
# print("Hallo" + " " + "Welt" + "!")
# print()
# print("Hallo" + " " + "Welt" + "!" * 3)
# print()
# print("Hallo" + " " + "Welt" + "!" * 3, "Hallo" + " " + "Welt" + "!" * 3)
# print()
from os.path import split

# Eine Variable definieren
y = "Hallo Welt!"
# Eine andere Variable definieren und die beiden Variablen zusammen ausgeben
# Konkatenation: Verkettung von Zeichenketten
x = "Python ist toll, oder!"
print(y + " " + x)
print() # Leerzeile
# Groß- und Kleinschreibung
print(x.upper())
print(x.lower())
# splitten: Aufteilen einer Zeichenkette
print(x.split(" "))
# an einer bestimmten Stelle einen Teil der Zeichenkette ausgeben
print(x[0]) # Erster Buchstabe
print(x[1]) # Zweiter Buchstabe
print(x.split(",")) # An dem Komma wird die Zeichenkette aufgeteilt5
print(x.split("toll")) # An dem Wort "toll" wird die Zeichenkette aufgeteilt
print()

# Ein Wort in einer Zeichenkette suchen
a = "Hallo Alberto"
print(a.find("Alberto"))  # Gibt die Position des Anfangs des Wortes zurück (6)
print(a[6:13])  # Gibt den Teil der Zeichenkette ab Position 6 aus
