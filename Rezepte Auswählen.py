print('AUSWAHL AN REZEPTEN')
print('Pfannkuchen Nr.1')
print('Waffeln Nr.2')
print('Käsekuchen Nr.3')

auswahl =  input('Bitte wähle deinen Rezept aus:')

print('Sie haben die auswahl möglichkeit Nr. ' + auswahl + ' ausgewählt')

if auswahl =='1':
    print('Pfannkuchen Rezept:')
    print('2 Eier - 200ml Milch - 150g Mehl - Prise Salz - Etwas Butter zum Braten')

elif auswahl =='2':
    print('Waffel Rezept:')
    print('3 Eier - 125g Zucker - 250g Mehl - 100g Butter - 1 TL Backpulver - 250ml Milch')

elif auswahl== '3':
    print('Käsekuchen Rezept:')
    print('500g Quark - 150g Zucker - 3 Eier - 1 Päckchen Vanillezucker - 1 Päckchen Puddingpulver - 100ml Öl')

else:
    print('Keine gültige Angabe.')

print('')

print("Mehr auf OlcayProjekt/GitHub")
input("Bitte belibige Taste drücken...")


