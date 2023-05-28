from datetime import date

def sprawdz_pełnoletniość(rok_urodzenia):
    aktualna_data = date.today()
    rok_bieżący = aktualna_data.year

    if rok_bieżący - rok_urodzenia >= 18:
        return True
    else:
        return False

def main():
    try:
        rok_urodzenia = int(input("Podaj rok urodzenia: "))
        if sprawdz_pełnoletniość(rok_urodzenia):
            print("Jesteś pełnoletni.")
        else:
            print("Nie jesteś pełnoletni.")
    except ValueError:
        print("Wprowadzono niepoprawny rok urodzenia.")

if __name__ == "__main__":
    main()


