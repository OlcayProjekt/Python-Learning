todos = ['Einkaufen','Steuerhinterziehen']

print("TODO LISTE")
newitem = input("Was möchtest du hinzufügen?")
todos.append(newitem)
print("Meine Liste hat diese Elemente:")

for todo in todos:
    print(f"-  {todo}")

print('')

newitem = input("Möchtest du noch was hinzufügen?")

todos.append(newitem)
print("Meine Liste hat diese Elemente:")

for todo in todos:
    print(f"-  {todo}")

print('')

print("Mehr auf OlcayProjekt/GitHub")
print("Programm beendet.")


