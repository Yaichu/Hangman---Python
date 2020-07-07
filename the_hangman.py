from collections import OrderedDict
import os.path

HANGMAN_PHOTOS = {1: """    x-------x""",
                  2: """    x-------x
    |
    |
    |
    |
    |
""",
                  3: """    x-------x
    |       |
    |       0
    |
    |
    |
""",
                  4: """    x-------x
    |       |
    |       0
    |       |
    |
    |
""",
                  5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""",
                  6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""",
                  7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""
                  }


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


def welcome():

    HANGMAN_ASCII_ART = """      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
    print(HANGMAN_ASCII_ART)


#######################################################################################################################
#######################################################################################################################

def choose_word(file_path, index):
    """ Returns a word from a file by it's index.
        :param file_path (string): the path of the file
        :param index (int): the index of the word in the file
        :return (string): the chosen word"""

    with open(file_path, "r") as input_file:
        file_content = input_file.read()
    # nodup = " ".join(OrderedDict.fromkeys(file_content.split()))  # new content without duplicates - with order

    # gets the word from a cyclic representation of the file
    word = file_content.split()[index % len(file_content.split()) - 1]
    return word


def show_hidden_word(secret_word, old_letters_guessed):
    """ Returns the current state of the word with underscores instead of the unguessed letters.
        :param secret_word (string): the word
        :param old_letters_guessed (list of chars): list of letters that were already guessed
        :return (string): the underscored word"""

    new_str = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            new_str = new_str + letter
        else:
            new_str = new_str + "_"
        new_str = new_str + " "
    new_str = new_str[:-1]
    return new_str


def is_valid_input(letter_guessed, old_letters_guessed):
    """ Checks if the letter is valid - is alphabetical and not already guessed.
        :param letter_guessed (string): the letter
        :param old_letters_guessed (list of chars): list of letters that were already guessed
        :return (bool): valid - True; else - False"""

    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ Tries to insert a letter to the list of guessed letters.
        If failed, the function prints the list of used letters.
        :param letter_guessed (string): the letter
        :param old_letters_guessed (list of chars): list of letters that were already guessed
        :return (bool): if succeeded to update the list  - True; else - False"""

    if is_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    old_letters_print = sorted(old_letters_guessed)
    old_letters_print = " -> ".join(old_letters_print)
    print(old_letters_print)
    return False

def check_win(secret_word, old_letters_guessed):
    """ Checks if the player won the game - all the letters of the word were guessed.
        :param secret_word (string): the word
        :param old_letters_guessed (list of chars): list of letters that were already guessed
        :return (bool): win - True; else - False"""

    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True



def main():
    ## Start of the game ##

    welcome()
    while True:  # takes care of invalid file path
        path = input("Enter file path: ")
        if os.path.isfile(path):
            break
        else:
            print("The file does not exist, try again!")
    index = int(input("Enter index: "))
    secret_word = choose_word(path, index)
    print("\nLet’s start!\n")

    hangman_state = 1
    print_hangman(hangman_state)
    print(show_hidden_word(secret_word, []))
    print("\n")

    ## Guess letters ##

    old_letters = []
    MAX_TRIES = 6
    while True:
        letter = input("Guess a letter: ").lower()
        is_legal = try_update_letter_guessed(letter, old_letters)
        if is_legal:
            if letter in secret_word:
                print(show_hidden_word(secret_word, old_letters))
            else:
                print(":(")
                hangman_state += 1
                print(HANGMAN_PHOTOS[hangman_state])

        is_winning = check_win(secret_word, old_letters)
        if is_winning:
            print("WIN")
            break
        else:
            if hangman_state == MAX_TRIES:
                print("LOSE")
                break




if __name__ == "__main__":
    main()