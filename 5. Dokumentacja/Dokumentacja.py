def dodawanie(a: float, b: float) -> float:
    return a + b
"""Dodaje dwie liczby.

    Args:
        a (float): Pierwsza liczba.
        b (float): Druga liczba.

    Returns:
        float: Wynik dodawania.
    """

def odejmowanie(a: float, b: float) -> float:
    return a - b
"""Odejmuje jedną liczbę od drugiej.

    Args:
        a (float): Pierwsza liczba.
        b (float): Druga liczba.

    Returns:
        float: Wynik odejmowania.
    """

def mnozenie(a: float, b: float) -> float:
    return a * b
"""Mnoży dwie liczby.

    Args:
        a (float): Pierwsza liczba.
        b (float): Druga liczba.

    Returns:
        float: Wynik mnożenia.
    """

def dzielenie(a: float, b: float):
    if b == 0:
        print("Nie można dzielić przez zero!")
        return None
    else:
        return a / b
    """Dzieli jedną liczbę przez drugą.

    Args:
        a (float): Pierwsza liczba.
        b (float): Druga liczba.

    
    """

def menu():
    print("Wybierz operację:")
    print("1 - Dodawanie")
    print("2 - Odejmowanie")
    print("3 - Mnożenie")
    print("4 - Dzielenie")
    print("0 - Wyjście")

def pobierz_liczby():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    return a, b

while True:
    menu()
    wybor = input("Twój wybór: ")

    if wybor == "0":
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
