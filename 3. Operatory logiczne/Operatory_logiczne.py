
inputUserAge = int(input("Ile masz lat? : "))

czyA2 = True if input("Czy masz prawo jazdy kat. A2 (t/n): ") \
    in ("t", "T", "Tak") else False
odIlu2 = 0
if czyA2:
    ofilu = int(input("Jak dlugo masz A2? Podaj ilosc lat: "))

if inputUserAge >= 24 or (czyA2 and inputUserAge >=20 and odIlu2 >=2):
    print("Mozesz przystąpić")
    pass
else:
    print("Nie moesz przystąpić")