word = input("Please enter a word: ")
solved_word = "_" * len(word)
solved_word = " ".join(solved_word)
print(solved_word)

letter = input("Guess a letter: ").lower()
print("The letter is: " + letter)




#3.2.1
# print("\"Shuffle, Shuffle, Shuffle\", say it together!\nChange colors and directions,\nDon't back down and stop the player!\n\tDo you want to play Taki?\n\tPress y\\n")

#3.3.3
# encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
# print(encrypted_message[-1::-2])
# >> I am learning python slicing!

#3.4.2
# string = input("Please enter a string: ")
# firstchar = string[0]
# new_string = string[1:].replace(firstchar, "e")
# print(firstchar + new_string)

#3.4.3
# string = input("Please enter a string: ")
# string_len = len(string)
# lowerString = string.lower()
# upperString = string.upper()
# half_string = string_len - (string_len//2)
# new_string = lowerString[:half_string] + upperString[half_string:]
# print(new_string)
# >> astronaut -> astroNAUT