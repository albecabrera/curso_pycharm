print("Hello World")
x = "Alberto"
print(x)
# Hola
print(x[2:5])
age = 47
print(age)
print(len(x))
y = "Dieser Satz ist recht lang. Wie lange ist er?"
print(len(y))
print("Der String mit der Variable y ist ", len(y), "Zeichen lang.")
z = "hallo"
z = "H" + z[1:]
print(z)

# Eine Schleife
for i in range(5):
    print("Python ist eine tolle Programmiersprache!")

for x in range(5):
    print("Hola mundo!")
    
for y in range(4):
    print("😀")

print()

# Schleife, die die Zahlen von 0 bis 9 ausgibt
for i in range(10):
    print(i+1)

print() # Fügt eine leere Zeile ein

# Code für die 7er-Reihe
for x in range(10):
    print((x+1)*7)

for acht in range(10):
    print((acht+1)*8)

print()

# Eine Zeichenkette 4-mal ausgeben
text = input("Was soll wiederholt werden: ")
anzahl = int(input("Wie oft: "))
for i in range(4):
    print(text)
    
print()
# # Eine andere Zeichenkette 6-mal in der Konsole ausgeben
# text2 = input("Füge eine Programmiersprache ein: ")
# anzahl = int(input("Welche:"))
# for t in range(6):
#     print(text2)

# While-Schleife
t = 8
while t <= 10:
    print(t)
    t = t + 1

print()

text3 = input("Was soll wiederholt werden?: ")
anzahl3 = int(input("Wie oft: "))

u = 1
while u <= anzahl3:
    print(u)
    u = u + 1

print()
i = 0
while i < 5:
    print(i)

    i += 1

print()

zaehler = 0
ergebnis = 0
schleifendurchlauefe = 0

while zaehler < 5:
    ergebnis = ergebnis + 1
    zaehler = zaehler + 1
    schleifendurchlauefe = schleifendurchlauefe + 1
print("Fertig! Ergebnis = ", ergebnis)
print("Schleifendurchläufe = ", schleifendurchlauefe)
print("Zähler =", zaehler)

print()

for e in range(7,71,7):
    print(e)

# Schleife while
n = 7
while n < 71:
    print(n)
    n = n + 7






