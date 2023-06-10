import random
import string
import os
import time


def display_game_rules():
    print()
    print("RULES OF THE GAME:")
    time.sleep(1)
    print()
    time.sleep(1)
    print("1. Guess the letters of the word displayed in blank spaces below.")
    time.sleep(1)
    print()
    print("2. Only guess alphabetical letters.")
    time.sleep(1)
    print()
    print("3. Numbers, spaces, punctuation, and blank guesses are not allowed.")
    time.sleep(1)
    print()
    print("4. You have 7 guesses to complete the word.")
    time.sleep(1)
    print()
    time.sleep(1)
    print("Good luck!")
    print()
    time.sleep(1)


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


def success():
    display_success = """   
 __          __  _ _    _____                     _   _   _ 
 \ \        / / | | |  |  __ \                   | | | | | |
  \ \  /\  / /__| | |  | |  | | ___  _ __   ___  | | | | | |
   \ \/  \/ / _ \ | |  | |  | |/ _ \| '_ \ / _ \ | | | | | |
    \  /\  /  __/ | |  | |__| | (_) | | | |  __/ |_| |_| |_|
     \/  \/ \___|_|_|  |_____/ \___/|_| |_|\___| (_) (_) (_)
"""                                                            
    print(display_success)                                                           


def game_over():
    display_game_over = """
    
 __          _____                          ____                         __
 \ \   _    / ____|                        / __ \                   _   / /
  | | (_)  | |  __  __ _ _ __ ___   ___   | |  | |_   _____ _ __   (_) | | 
  | |      | | |_ |/ _` | '_ ` _ \ / _ \  | |  | \ \ / / _ \ '__|      | | 
  | |  _   | |__| | (_| | | | | | |  __/  | |__| |\ V /  __/ |      _  | | 
  | | (_)   \_____|\__,_|_| |_| |_|\___|   \____/  \_/ \___|_|     (_) | | 
 /_/                                                                    \_\
                                                                           
"""
    print(display_game_over)


def lets_go():
    display_lets_go = """
    
  _          _   _        _____                                 _   _   _ 
 | |        | | ( )      / ____|                               | | | | | |
 | |     ___| |_|/ ___  | |  __  ___   ___   ___   ___   ___   | | | | | |
 | |    / _ \ __| / __| | | |_ |/ _ \ / _ \ / _ \ / _ \ / _ \  | | | | | |
 | |___|  __/ |_  \__ \ | |__| | (_) | (_) | (_) | (_) | (_) | |_| |_| |_|
 |______\___|\__| |___/  \_____|\___/ \___/ \___/ \___/ \___/  (_) (_) (_)
                                                                          
"""
    print(display_lets_go)


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


def lost_game_prompt():
    time.sleep(2)
    print()
    print("But that's okay, your time will come!!")
    print()
    time.sleep(1)
    print("Let's give it another go, yeah?")
    time.sleep(1)
    print()
    print("Type 'yes' to go again or 'no' to quit")
    print()
    user_choice = ''
    user_name = ''
    while user_choice == '':
        user_choice = input().lower().strip()
        if user_choice in ['yes']:
            lets_go()
            display_game_rules()
            run_hangman_game(user_name)
            user_choice = ''
        elif user_choice in ['no']:
            print(f'See you next time {user_name}!')
            exit()
        else:
            print('Please type "yes" to play, '
                  'or "no" to quit.')
            user_choice = ''


def won_game_prompt():
    time.sleep(2)
    print()
    print("Sensational stuff!! Your guesswork is impecable.")
    time.sleep(1)
    print()
    print("I would love to see you do it again!")
    time.sleep(1)
    print()
    print("type 'yes' to go again or 'no' to quit")
    print()
    user_choice = ''
    user_name = ''
    while user_choice == '':
        user_choice = input().lower().strip()
        if user_choice in ['yes']:
            lets_go()
            display_game_rules()
            run_hangman_game(user_name)
            user_choice = ''
        elif user_choice in ['no']:
            print(f'See you next time {user_name}!')
            exit()
        else:
            print('Please type "yes" to play, '
                  'or "no" to quit.')
            user_choice = ''


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
        user_choice = input(f"Hello and welcome, {user_name}! "
                            "Do you fancy a game of hangman? "
                            "Type 'yes' to play,"
                            "or 'no' to quit: ").lower().strip()

        if user_choice in ['yes']:
            display_game_rules()
            run_hangman_game(user_name)
            user_choice = ''
        elif user_choice in ['no']:
            print(f'See you next time {user_name}!')
            exit()
        else:
            print('Please type "yes" to play, '
                  'or "no" to quit.')
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
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please enter only one letter."
                  "Spaces and blank attempts not allowed")
            continue

        if not guess.isalpha():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please enter only alphabetical characters.")
            continue

        if guess in guessed_correct or guess in guessed_incorrect:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You have already guessed that letter. Try another letter.")
            continue

        if guess in word:
            guessed_correct.append(guess)
            for i in range(len(word)):
                if word[i] == guess:
                    word_progress[i] = guess
            if '_' not in word_progress:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"The word was: {word}")
                success()
                print("Congratulations, you guessed the word correctly!")
                won_game_prompt()
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Good guess! Let's go again.")
        else:
            guessed_incorrect.append(guess)
            hangman_count += 1
            guesses -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Wrong guess! Let's try again.")

    if guesses == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        game_over()
        print_hangman_art(hangman_count)
        print(f"Oops! You ran out of tries {user_name}. The word was:", word)
        lost_game_prompt()