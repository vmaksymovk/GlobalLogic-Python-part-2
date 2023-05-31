import os
from os.path import dirname, join
import string

file_path = join(dirname(__file__), "tekst.txt")

def count_words(file_path):
    word_count = 0
    ending_stats = {}

    with open(file_path, 'r') as file:
        paragraphs = file.read().split("\n\n")

        for paragraph in paragraphs:
            words = paragraph.split()

            for word in words:
                word = word.strip(string.punctuation)
                if word:
                    word_count += 1
                    last_letter = word[-1].lower()

                    if last_letter in ending_stats:
                        ending_stats[last_letter] += 1
                    else:
                        ending_stats[last_letter] = 1

    return word_count, ending_stats

word_count, ending_stats = count_words(file_path)

print(f"Liczba słów w tekście: {word_count}")
print("Statystyki końcówek słów:")
print(ending_stats)
