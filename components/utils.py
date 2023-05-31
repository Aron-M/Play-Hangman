def get_words(filepath='words.txt'):
    result = []
    with open(filepath) as n:
        lines = n.readlines()
        for line in lines:
            word = str(line).lower().strip()
            result.append(word)
        return result


def initialize_game():
    user = ''
    while user == '':
        user = input("Hello and welcome! Do you fancy a game of hangman? Type 'yes'or 'start' to play. If not, type 'exit' or 'no' to quit").lower().strip()
        if user == 'yes' or user == 'start':
            run_hangman_game()
            user = ''
        if user == 'exit' or user == 'no':
            print('See you next time!')
            exit()
        else:
            print('Please type y or yes to play, else type n or no to quit.')
            user = ''
