import random
from hangman_ascii_art import print_hangman_art
from utils import get_words, initialize_game, run_hangman_game, guessed_correct, guessed_incorrect


initialize_game()

def run_hangman_game(user_name):
    user_name = ''
    words = get_words()
    word = random.choice(words).lower().strip()
    word_progress = ['_'] * len(word)
    amount_correct = []
    amount_incorrect = []
    guesses = 7
    hangman_count = -1

    while guesses > 0:
        print_hangman_art(hangman_count)
        print("Guessed Correct:", amount_correct)
        print("Guessed Incorrect:", amount_incorrect)
        print("Tries left:", guesses)
        print("Word progress:", ' '.join(word_progress))

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in amount_correct or guess in amount_incorrect:
        print("You have already guessed that letter.")
        continue

    if guess in word:
        guessed_correct()