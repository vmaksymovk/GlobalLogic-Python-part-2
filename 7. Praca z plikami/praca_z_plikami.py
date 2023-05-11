
def count_words_and_last_letters(filename):
    word_count = 0
    last_letters_count = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_count += 1
                last_letter = word[-1].lower()
                if last_letter.isalpha():
                    if last_letter in last_letters_count:
                        last_letters_count[last_letter] += 1
                    else:
                        last_letters_count[last_letter] = 1
    print(f"Liczba słow: {word_count}")
    print("Statystyka:")
    for letter, count in sorted(last_letters_count.items()):
        print(f"{letter}: {count}")

count_words_and_last_letters("/Users/vlad/Desktop/Python_part_2/Python_part_2/7. Praca z plikami/tekst.txt")


