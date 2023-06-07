import random


def print_hangman_art(hangman_count):
    hangman_image = [
        """
        +---+
          | |
          O |
            |
            |
            |
         ======
        """, 

        """
        +---+
          | |
          O |
         /  |
            |
            |
         ======
        """, 

        """
        +---+
          | |
          O |
         /| |
            |
            |
         ======
        """, 

        """
        +---+
          | |
          O |
         /|\|
            |
            | 
         ======
        """, 

        """
        +---+
          | |
          O |
         /|\|
          | | 
            | 
         ======
        """, 

        """
        +---+
          | |
          O |
         /|\|
          | | 
         /  | 
         ======
        """, 

        """
        +---+
          | |
          O |
         /|\|
          | | 
         / \| 
         ======
        """
    ]

    print(hangman_image[hangman_count])



def get_words(filepath='/workspace/Play-Hangman/words.txt'):
    result = []
    with open(filepath) as n:
        lines = n.readlines()
        for line in lines:
            word = str(line).lower().strip()
            result.append(word)
        return result


def initialize_game():
    user_name = input("Hello and welcome! Please enter your name: ")

    user_choice = ''
    while user_choice == '':
        user_choice = input(f"Hello, {user_name}! "
                            "Do you fancy a game of hangman? "
                            "Type 'yes' or 'start' to play. "
                            "If not, type 'exit' "
                            "or 'no' to quit: ").lower().strip()

        if user_choice in ['yes', 'start']:
            run_hangman_game(user_name)
            user_choice = ''
        elif user_choice in ['exit', 'no']:
            print('See you next time!')
            exit()
        else:
            print('Please type "yes" or "start" to play, '
                  'or "exit" or "no" to quit.')
            user_choice = ''


def run_hangman_game(user_name):
    words = get_words()
    word = random.choice(words).lower().strip()
    word_progress = ['_'] * len(word)
    guessed_correct = []
    guessed_incorrect = []
    guesses = 7
    hangman_count = -1

    while guesses > 0:
        print_hangman_art(hangman_count)
        print("Guessed Correct:", guessed_correct)
        print("Guessed Incorrect:", guessed_incorrect)
        print("Tries left:", guesses)
        print("Word progress:", ' '.join(word_progress))

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if guess in guessed_correct or guess in guessed_incorrect:
            print("You have already guessed that letter.")
            continue

        if guess in word:
            guessed_correct.append(guess)
            for i in range(len(word)):
                if word[i] == guess:
                    word_progress[i] = guess
            if '_' not in word_progress:
                print("Congratulations, you guessed the word correctly!")
                break
        else:
            guessed_incorrect.append(guess)
            hangman_count += 1
            guesses -= 1
            print("Wrong guess!")

    if guesses == 0:
        print_hangman_art(hangman_count)
        print("Oops! You ran out of tries. The word was:", word)