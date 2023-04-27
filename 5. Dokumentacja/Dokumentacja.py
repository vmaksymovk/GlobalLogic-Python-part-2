
"""Definicja funkcji calc"""
def calc():

    """Informacja dla uzytkownika"""
    print('Ten program - \'kalkulator \' \nDla wyjscia wpisz \'s\'')

    """Wyłowanie pętli nieskończonej"""
    while True:

        """Input od uzytkownika"""
        a = input("Napisz wyrazenie (Naprzykład: 40 - 34): ")

        """Sprawdzanie warunku czy uzytkownik chce wyjsc"""
        if a == "s":


            print('Dziękuje za skorzystanie z programy!')


            break

            """Nasz kalkulator"""
        print(a + " = " + str(eval(a)))

"""Wyłołanie funkcji"""      
calc()

    
    