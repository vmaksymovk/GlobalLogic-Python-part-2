import os
from os.path import dirname, join
import random

imiona_file = join(dirname(__file__), "imiona.txt")
nazwiska_file = join(dirname(__file__), "nazwiska.txt")
output_file = join(dirname(__file__), "kombinacje.txt")

def generate_combinations(imiona_file, nazwiska_file, output_file, liczba_kombinacji):
    with open(imiona_file, 'r', encoding='utf-8') as imiona, \
         open(nazwiska_file, 'r', encoding='utf-8') as nazwiska, \
         open(output_file, 'w', encoding='utf-8') as output:

        lista_imion = [line.strip() for line in imiona.readlines()]
        lista_nazwisk = [line.strip() for line in nazwiska.readlines()]

        random.shuffle(lista_imion)
        random.shuffle(lista_nazwisk)

        for i in range(liczba_kombinacji):
            imie = lista_imion[i % len(lista_imion)]
            nazwisko = lista_nazwisk[i % len(lista_nazwisk)]
            kombinacja = f"{imie} {nazwisko}\n"
            output.write(kombinacja)

    print(f"Pomyślnie wygenerowano i zapisano {liczba_kombinacji} kombinacji imion i nazwisk.")

liczba_kombinacji = int(input("Podaj liczbę kombinacji do wygenerowania: "))
generate_combinations(imiona_file, nazwiska_file, output_file, liczba_kombinacji)
