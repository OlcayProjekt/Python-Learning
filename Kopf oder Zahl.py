print("Kopf oder Zahl")

print("")

Name = input("Gebe deinen Namen ein: ")
print ("Salut, Mr" + Name )

print("")

print("Heute ist der Tag wo du deine wichtigste Entscheidung treffen wirst.")
print("Kopf oder Zahl?")

print("")

Auswahl = input("Gebe ein was du auswählst " + Name +" (Kopf/Zahl): ")

if Auswahl == 'Kopf':
    print("Glück gehabt heute kommst du davon...")

if Auswahl =='Zahl':
    print("Deine Tage sind auch gezählt...")

print('')

if Auswahl == 'Kopf':
    print("Lass uns noch eine Runde spielen.")

wurf = input("Kopf oder Zahl: ")

import random

wurf = random.randint(1, 2)

if wurf == 1:
    print("Gut Gemacht " + Name +", du hast Kopf bekommen")

else:
    print("Opps " + Name +", du hast Zahl bekommen")

print("")

last = input("Was hälst du davon wenn wir ein letztes mal um die Münze spielen? (ja/nein) ")

if last == "ja":
    print("Kopf oder ZAHL?")

if last == "nein":
    print("war eine tolle Zeit mit dir.")




print("")
print("Mehr auf OlcayProjekt/GitHub")
input("🔚Bitte belibige Taste drücken...")