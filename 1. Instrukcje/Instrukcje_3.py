# Zadanie 3
import random

randomValue = random.randint(0, 10)
i = 0

while True:
    userInput = int(input("Sproboj zgadnąć liczbę: "))
    if userInput < randomValue:
        print("Liczba jest mniejsza od podanej!")
        i += 1
    elif userInput > randomValue:
       print("Liczba jest większa od podanej!") 
       i += 1
    elif userInput == randomValue:
        print("Dokonales " + str(i) + " sprob")
        break


