def calc():
    print('Ten program \'kalkulator \' \nDla wyjscia wpisz \'s\'')
    while True:
        a = input("Napisz wyrazenie (Naprzykład: 40 - 34): ")
        if a == "s":
            print('Dziękuje za skorzystanie z programy!')
            break
        print(a + " = " + str(eval(a)))
calc()

    
    