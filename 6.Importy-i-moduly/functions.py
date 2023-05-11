

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        print("Nie można dzielić przez zero!")
        return None
    else:
        return a / b

def menu():
    print("Wybierz operację:")
    print("1 - Dodawanie")
    print("2 - Odejmowanie")
    print("3 - Mnożenie")
    print("4 - Dzielenie")
    print("q - Wyjście")

def pobierz_liczby():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    return a, b