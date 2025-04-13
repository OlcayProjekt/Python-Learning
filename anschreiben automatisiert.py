str = input("Bitte gebe den Namen ein: ")
age = input("Trage deinen alter ein: ")
City = input("Trage ein in welcher Stadt du lebst: ")
Schule= input("Welche Schule besuchst du zurzeit: ")
name= input("Wie heißt die Person die das anschreiben bekommen soll: ")
Anrede="Herr"

is_woman = False

if is_woman:
    print("Sehr geehrte Frau" + name +",")
else:
    print("Sehr geehrter Herr" + name +",")
print("")
print("mein Name ist " + str +".")
print("Ich bin " + age + " Jahre alt.")
print("Ich lebe in der Stadt " +City+ " zurzeit.")
print("Ich gehe zur " +Schule+ " Schule in " +City)

print("Mehr auf OlcayProjekt/GitHub")
input("Bitte belibige Taste drücken...")