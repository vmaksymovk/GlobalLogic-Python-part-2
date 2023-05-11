class Czytelnik:
    def __init__(self, imie, nazwisko, numer_karty):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_karty = numer_karty

    def __str__(self):
        return f"Czytelnik: {self.imie} {self.nazwisko}, numer karty: {self.numer_karty}"


czytelnik1 = Czytelnik("Jan", "Kowalski", "22222")
czytelnik2 = Czytelnik("Anna", "Nowak", "111111")


print(czytelnik1)
print(czytelnik2)
