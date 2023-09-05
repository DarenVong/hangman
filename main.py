# Choose a list of words as the game's word bank.
# Create a function to select a random word from the word bank.
# Display a series of underscores representing the letters in the word to be guessed.
# Allow the player to guess letters one at a time.
# Check if the guessed letter is in the word and reveal its position(s) if correct.
# Keep track of the number of incorrect guesses and limit the player to a certain number of attempts (e.g., 6 for the hangman body parts).
# Display the hangman figure as the player makes incorrect guesses (you can use ASCII art for this).
# End the game when the player either guesses the word correctly or runs out of attempts.
# Provide a way for the player to play again if they wish.


from scripts import hangman_code
from scripts import print_hangman
import time

word_bank = hangman_code.read_text_files("wordbank.txt")

while True:
    print_hangman.menu()
    start_game = int(input("start game press 1 , press 0 exit\n"))
    if start_game == 1:
        lives = 6
        display_word = ""
        guessed_letters = []
        correct_index_array = []
        word = hangman_code.random_word(word_bank)
        print(word)
        hidden_word = hangman_code.hide_word(word)
        print(f"Guessed letters: {guessed_letters}")
        print(hidden_word)
        while True:
            print_hangman.print_gamestate(lives)
            print(guessed_letters)
            print(word)
            print(display_word)
            guess = input("Guess a letter ")
            success = 0
            for letter in range(len(word)):
                if guess == word[letter]:
                    success = 1
                    correct_index_array.append(letter)

            if success == 0:
                print(f"Letter: {guess} is not in the word")
                lives -= 1

            guessed_letters.append(guess)
            display_word = ""
            for i in range(len(word)):
                if i in correct_index_array:
                    display_word += word[i]
                else:
                    display_word += '_'
            if len(word) == len(correct_index_array):
                print("You win!")
                time.sleep(3)
                break
            if lives == 0:
                print_hangman.print_gamestate(lives)
                # print_hangman.gamephase6()
                print(f"The word was {word}")
                print("You lost")
                time.sleep(3)
                break
            # print(word)
            # print(correct_index_array)
    elif start_game == 0:
        exit()
    else:
        print("Invalid input")



