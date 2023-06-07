import random
import string


def display_game_rules():
    print()
    print("RULES OF THE GAME:")
    print()
    print("1. Guess the letters of the word displayed in blank spaces below.")
    print("2. Only guess lower-case alphabetical letters.")
    print("3. Numbers, spaces, punctuations, blank guesses are not allowed.")
    print("4. You have 7 guesses to complete the word.")
    print()
    print("Good luck!")


def display_game_title():
    game_title = """


  _____ _   _        _    _                                         
 |_   _| | ( )      | |  | |                                        
   | | | |_|/ ___   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
   | | | __| / __|  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  _| |_| |_  \__ \  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_____|\__| |___/  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                         __/ |                      
                                        |___/                       
                
                      _______ _                  _ 
                     |__   __(_)                | |
                        | |   _ _ __ ___   ___  | |
                        | |  | | '_ ` _ \ / _ \ | |
                        | |  | | | | | | |  __/ |_|
                        |_|  |_|_| |_| |_|\___| (_)
    """
    print(game_title)


def print_hangman_art(hangman_count):
    hangman_image = [
        """
        +---+
            |
            |
            |
            |
            |
         ======
        """,
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


def get_words(filepath='words.txt'):
    result = []
    with open(filepath) as n:
        lines = n.readlines()
        for line in lines:
            word = str(line).lower().strip()
            result.append(word)
        return result


def initialize_game():
    display_game_title()
    user_name = input("Hello and welcome! Please enter your name: ")

    if not user_name.strip():
        print("User name cannot be blank. Please enter a valid name.")
        return

    if any(char in string.punctuation for char in user_name):
        print("User name cannot contain punctuation marks."
              "Please enter a valid name.")
        return

    user_choice = ''
    while user_choice == '':
        user_choice = input(f"Hello, {user_name}! "
                            "Do you fancy a game of hangman? "
                            "Type 'yes' or 'start' to play. "
                            "If not, type 'exit' "
                            "or 'no' to quit: ").lower().strip()

        if user_choice in ['yes', 'start']:
            display_game_rules()
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
    hangman_count = 0

    while guesses > 0:
        print_hangman_art(hangman_count)
        print("Guessed Correct:", guessed_correct)
        print("Guessed Incorrect:", guessed_incorrect)
        print("Tries left:", guesses)
        print("Word progress:", ' '.join(word_progress))
        print()
        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter only one letter."
                  "Spaces and blank attempts not allowed")
            continue

        if not guess.isalpha():
            print("Please enter only alphabetical characters.")
            continue

        if guess in guessed_correct or guess in guessed_incorrect:
            print("You have already guessed that letter. Try another letter.")
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
            print("Wrong guess! Let's go again.")

    if guesses == 0:
        print_hangman_art(hangman_count)
        print("Oops! You ran out of tries. The word was:", word)