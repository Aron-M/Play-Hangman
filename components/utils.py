def get_words(filepath='words.txt'):
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
        user_choice = input(f"Hello, {user_name}!"
                            "Do you fancy a game of hangman? "
                            "Type 'yes' or 'start' to play. "
                            "If not, type 'exit'" 
                            "or 'no' to quit: ").lower().strip()
        
        if user_choice in ['yes', 'start']:
            run_hangman_game(user_name)
            user_choice = ''
        elif user_choice in ['exit', 'no']:
            print('See you next time!')
            exit()
        else:
            print('Please type "yes" or "start" to play,'
                  'or "exit" or "no" to quit.')
            user_choice = ''


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


def guessed_correct():
    if letter in word_progress:
        output += letter
        
    while guess in word:
        print(f"Well done {user_name}, "
              "you guessed a correct letter!" + '\U0001F44F' * 3)
        guessed_correct.append(guess)
        print(word_progress)
        user_choice = ''

