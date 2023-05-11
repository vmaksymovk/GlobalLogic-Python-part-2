from functions import *

while True:
    menu()
    wybor = input("Twój wybór: ")

    if wybor == "q":
        print("Koniec programu.")
        break

    if wybor in ["1", "2", "3", "4"]:
        a, b = pobierz_liczby()

        if wybor == "1":
            wynik = dodawanie(a, b)
            print("Wynik dodawania:", wynik)

        elif wybor == "2":
            wynik = odejmowanie(a, b)
            print("Wynik odejmowania:", wynik)

        elif wybor == "3":
            wynik = mnozenie(a, b)
            print("Wynik mnożenia:", wynik)

        elif wybor == "4":
            wynik = dzielenie(a, b)
            if wynik is not None:
                print("Wynik dzielenia:", wynik)

    else:
        print("Nieprawidłowy wybór.")
