print("Schreibe namen auf die du beleidigen möchtest.")
beleidigung = input("Schreibe deine ausgewählte beleidigung auf:")
name_der_person = input("Trage den Namen der Person ein:")

print('')
print(name_der_person + ", du " + beleidigung + "!")
print('')

name = input ("👀 Trage deinen Namen ein um weiterzumachen:")
repeat = input("🔁 Möchtest du diesen Satz wiederholen " +  name +"? (ja/nein): ").lower()

print('')

if repeat =='ja':
    how_often = input("Wie oft soll der Satz ausgeführt werden " + name + "? (zahl): ")

    if how_often.isdigit():
        print("Deine Beleidigung wird " +how_often + " wiederholt")
        for _ in range(int(how_often)):
            print(name_der_person + ", du " + beleidigung + "!")
    else:
      print("Bitte gib eine gültige Zahl ein!")

elif repeat =='nein':
    print("🫡Verstanden Chef, starte das Programm neu wenn du, von vorne anfangen willst.")

else:
    print("❓ Ungültige Eingabe – bitte nur 'ja' oder 'nein' eingeben.")

print('')

input("🔚Bitte belibige Taste drücken...")



