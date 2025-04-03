start_price = 4.80
km = int(input("Bitte Kilometer eingeben: "))
if km > 5:
    costs = 1.90
else:
    costs = 2.10

total_expenses = start_price + costs * km

print("Deine Kosten liegen bei unglaublichen", total_expenses)