def mnozenie(a, b):
    if a is None or b is None:
        return None
    return a * b


def dodawanie(a, b):
    try:
        if a is None or b is None:
            raise ValueError("Nieprawidłowe argumenty!")
        return a + b
    except Exception as e:
        print("Wystąpił błąd podczas dodawania:", e)
        return None

def odejmowanie(a, b):
    try:
        if a is None or b is None:
            raise ValueError("Nieprawidłowe argumenty!")
        return a - b
    except Exception as e:
        print("Wystąpił błąd podczas odejmowania:", e)
        return None

def dzielenie(a, b):
    try:
        if a is None or b is None:
            raise ValueError("Nieprawidłowe argumenty!")
        if b == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero!")
        else:
            return a / b
    except ZeroDivisionError as e:
        print(e)
        return None
    except Exception as e:
        print("Wystąpił błąd podczas dzielenia:", e)
        return None



def menu():
    print("Wybierz operację:")
    print("1 - Dodawanie")
    print("2 - Odejmowanie")
    print("3 - Mnożenie")
    print("4 - Dzielenie")
    print("q - Wyjście")

def pobierz_liczby():
    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        return a, b
    except ValueError:
        print("Nieprawidłowy format liczby!")
        menu()
        return None, None




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
