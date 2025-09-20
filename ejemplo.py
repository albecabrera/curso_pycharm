from traceback import format_list

print("Hello World")
x = "Alberto"
print(x)
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
# text2 = input("Füge eine Programmiersprache ein:")
# anzahl = int(input("Welche:"))
# for t in range(6):
#     print(text2)

