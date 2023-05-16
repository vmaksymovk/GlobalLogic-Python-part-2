import random
from typing import List

# otwieramy pliki z imionami i nazwiskami
with open("/Users/vlad/Desktop/Python_part_2/Python_part_2/7. Praca z plikami/imiona.txt") as f:
    imiona = [line.strip() for line in f]

with open("/Users/vlad/Desktop/Python_part_2/Python_part_2/7. Praca z plikami/nazwiska.txt") as f:
    nazwiska = [line.strip() for line in f]

# pobieramy od użytkownika liczbę kombinacji
x = int(input("Podaj liczbę kombinacji: "))

# tworzymy listę kombinacji

kombinacje: List[str] = []
while len(kombinacje) < x:
    imie = random.choice(imiona)
    nazwisko = random.choice(nazwiska)
    kombinacja = f"{imie} {nazwisko}"
    if kombinacja not in kombinacje:
        kombinacje.append(kombinacja)

# zapisujemy kombinacje do pliku
with open("/Users/vlad/Desktop/Python_part_2/Python_part_2/7. Praca z plikami/kombinacje.txt", "w") as f:
    for kombinacja in kombinacje:
        f.write(kombinacja + "\n")
