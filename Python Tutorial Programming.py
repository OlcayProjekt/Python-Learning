print("TAXI DRIVER PREIS")
start_price = 4.80
km = int(input("Bitte Kilometer eingeben: "))

if km > 5:
    costs = 1.90
else:
    costs = 2.10

total_expenses = start_price + costs * km

print(f"Deine Kosten liegen bei unglaublichen {total_expenses:.2f}€")

print("Mehr auf OlcayProjekt/GitHub")
input("Bitte belibige Taste drücken...")