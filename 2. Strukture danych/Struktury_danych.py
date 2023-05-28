def znajdz_największą_najmniejszą(krotka):
    największa = krotka[0]
    najmniejsza = krotka[0]

    for liczba in krotka:
        if liczba > największa:
            największa = liczba
        if liczba < najmniejsza:
            najmniejsza = liczba

    return największa, najmniejsza

def main():
    krotka = (10, -3, 4, 9, 12, -6, 0)
    największa, najmniejsza = znajdz_największą_najmniejszą(krotka)

    print("Największa liczba: ", największa)
    print("Najmniejsza liczba: ", najmniejsza)

if __name__ == "__main__":
    main()
