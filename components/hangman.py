import random
from hangman_ascii_art import print_hangman_art
from utils import get_words

def run_hangman_game():
    hangman = print_hangman_art()

    words = get_words()
    word = random.choice(words).lower().strip()
    guessed_right = []
    guessed_wrong = []
    tries = 8
    hangman_count = -1