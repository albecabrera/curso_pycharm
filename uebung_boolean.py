# Kinder (U18) 5€
# Erwachsene 10€
# Senioren 7,50€


# Variante 1 Was kostet ein Ticket?
# Variante 2 Was kosten alle Tickets?

alter = int(input("Trage dein Alter ein: "))
anzahl = int(input("Wieviele Tickets möchtest du denn kaufen: "))
if alter > 65:
    print(7.5 * anzahl)
elif alter >= 18:
    print(10 * anzahl)
else:
    print(5 * anzahl)