
str = input("Wprowadz slowo: ")
reversed=''.join(reversed(str))
if reversed == str:
    print("Palindrom")
    pass
else:
    print("Nie palindrom")