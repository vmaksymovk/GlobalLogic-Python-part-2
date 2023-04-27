array = ['burak', 'cukinia', 'pomidor', 'cytryna', 'ananas', 'papryka', 'dynia']
litera = input("Wprowadz litere: ")

for element in array:
    if element.startswith(litera):
        print(element, end=" ")