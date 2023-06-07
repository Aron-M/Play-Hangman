import random
from hangman_ascii_art import print_hangman_art
from utils import get_words, initialize_game, guessed_correct, guessed_incorrect


user_name = ''
words = get_words()
word = random.choice(words).lower().strip()
amount_correct = []
amount_incorrect = []
guesses = 7
hangman_count = -1