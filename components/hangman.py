import random
from hangman_ascii_art import print_hangman_art
from utils import get_words

words = get_words()
word = random.choice(words).lower().strip()
guessed_correct = []
guessed_incorrect = []
guesses = 7
hangman_count = -1