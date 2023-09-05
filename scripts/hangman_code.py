import random
from scripts import print_hangman

def read_text_files(file_path):
    word_array = []
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            word_array.append(word)
    return word_array


def random_word(x):
    random_word = random.randint(1, len(x) - 1)
    return x[random_word]


def hide_word(word):
    return '_' * len(word)

# def guess_letter(letter, word):
#     success = 0
#     for i in range(len(word)):
#         if word[i] == letter:
#             success = 1
#             return i
#
#     if success == 0:
#         return -1
