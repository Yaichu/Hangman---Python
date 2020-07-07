from random import randrange

HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

print(HANGMAN_ASCII_ART)

MAX_TRIES = randrange(3, 7)
print("The number of tries allowed is: " + str(MAX_TRIES))

letter = input("Guess a letter: ")
print("The letter is: " + letter)
