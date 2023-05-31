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
        user_choice = input(f"Hello, {user_name}! Do you fancy a game of hangman? "
                            "Type 'yes' or 'start' to play. "
                            "If not, type 'exit' or 'no' to quit: ").lower().strip()
        
        if user_choice in ['yes', 'start']:
            run_hangman_game(user_name)
            user_choice = ''
        elif user_choice in ['exit', 'no']:
            print('See you next time!')
            exit()
        else:
            print('Please type "yes" or "start" to play, or "exit" or "no" to quit.')
            user_choice = ''



def start_round():
        for letter in word:
            if letter in guessed_correct:
                output += letter
        
        while guess in word:
            print("That was great! Well done, you guessed the right letter!")
            guessed_correct.append(guess)
            user_choice = ''

