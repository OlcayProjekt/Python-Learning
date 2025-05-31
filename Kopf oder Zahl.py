import random

print("Kopf oder Zahl\n")

Name = input("Gebe deinen Namen ein: ")
print("Salut, Mr " + Name + "\n")

print("Heute ist der Tag, wo du deine wichtigste Entscheidung treffen wirst.")
print("Kopf oder Zahl?\n")

Auswahl = input("Gebe ein was du auswählst, " + Name + " (Kopf/Zahl): ").strip().lower()

if Auswahl == 'kopf':
    print("Glück gehabt, heute kommst du davon...")
elif Auswahl == 'zahl':
    print("Deine Tage sind auch gezählt...")
else:
    print("Ungültige Eingabe.")

print('')

if Auswahl == 'kopf':
    print("Lass uns noch eine Runde spielen.")

benutzertipp = input("Kopf oder Zahl: ").strip().lower()
zufall = random.randint(1, 2)
ergebnis = "kopf" if zufall == 1 else "zahl"

print("Der Wurf ergibt:", ergebnis)

if benutzertipp == ergebnis:
    print("Gut gemacht, " + Name + "! Du hast richtig geraten.")
else:
    print("Opps, " + Name + ". Das war leider falsch.")

print("")

last = input("Was hältst du davon, wenn wir ein letztes Mal um die Münze spielen? (ja/nein) ").strip().lower()

if last == "ja":
    print("Okay, so langsam gewöhne ich mich an dich.")

elif last == "nein":
    print("War eine tolle Zeit mit dir.")

benutzertipp = input("Kopf oder Zahhhhhhll:").strip().lower()
zufall = random.randint(1,2)
ergebnis = "zahl" if zufall == 1 else "kopf"

print("Der Wurf ergibt," + ergebnis)

if benutzertipp == ergebnis:
    print("YEAH, du bist ein nartur talent...")

else:
    print("Kann vorkommen, kopf hoch")

print("")

print("Danke fürs mitspielen, Moniseur " + Name)

print("Mehr auf OlcayProjekt/GitHub")
input("🔚 Bitte beliebige Taste drücken...")

