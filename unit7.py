def show_hidden_word(secret_word, old_letters_guessed):
    new_str = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            new_str = new_str + letter
        else:
            new_str = new_str + "_"
        new_str = new_str + " "
    new_str = new_str[:-1]
    return new_str


print(show_hidden_word("mammals", ['s', 'y', 'j', 'i', 'm', 'k']))

def check_win(secret_word, old_letters_guessed):
    # option 1
    # if '_' in show_hidden_word(secret_word, old_letters_guessed):
    #     return False
    # return True

    # option 2
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

print(check_win("friends", ['m', 'p', 'j', 'i', 's', 'k']))
print(check_win("yes", ['m', 'p', 'j', 'i', 's', 'k', 'e', 'y']))



#7.1.4
# import math
# def squared_numbers(start, stop):
#     my_list = []
#     while start <= stop:
#         powed = int(math.pow(start, 2))
#         my_list.append(powed)
#         start += 1
#     return my_list
#
#
# print(squared_numbers(-3, 3))

#7.2.1
# def is_greater(my_list, n):
#     new_list = []
#     for i in my_list:
#         if i > n:
#             new_list.append(i)
#     return new_list
#
# print(is_greater([1, 30, 25, 60, 27, 28], 28))

#7.2.2
# def numbers_letters_count(my_str):
#     new_list = [0, 0]
#     for letter in my_str:
#         if letter.isnumeric():
#             new_list[0] += 1
#         else:
#             new_list[1] += 1
#     return new_list
#
#
# print(numbers_letters_count("Python 3.6.3"))

#7.2.4
# def seven_boom(end_number):
#     new_list = []
#     for num in range(end_number + 1):
#         if num % 7 == 0 or '7' in str(num):
#             new_list.append("BOOM")
#         else:
#             new_list.append(num)
#     return new_list
#
#
# print(seven_boom(17))

#7.2.5
# def sequence_del(my_str):
#     last_pushed_char = ''
#     new_str = ''
#     for letter in my_str:
#         if letter != last_pushed_char:
#             new_str += letter
#             last_pushed_char = letter
#     return new_str
#     # option 2
#     # new_str = ''
#     # for i in range(len(my_str) - 1):
#     #     if my_str[i] != my_str[i + 1]:
#     #         new_str = new_str + my_str[i]
#     # if my_str[-1] != my_str[-2]:
#     #     new_str = new_str + my_str[-1]
#     # return new_str
#     # option 3
#     # return "".join(dict.fromkeys(my_str))
#
# print(sequence_del("Heeyyy   yyouuuu!"))


#7.2.6
# def shopping(my_str):
#     digit = int(input("Enter a digit between 1-8: "))
#     my_list = my_str.lower().split(',')
#     while digit != 9:
#         # this is a switch on "digit"
#         if digit == 1:  # print list of products
#             print(my_list)
#         elif digit == 2:  # items total count
#             print(len(my_list))
#         elif digit == 3:  # checks whether item is the in list
#             item = input("Enter product name: ").lower()
#             print(item in my_list)
#         elif digit == 4:  # count of a product
#             item = input("Enter product name to see it's count: ").lower()
#             print(my_list.count(item))
#         elif digit == 5:  # remove a product from list
#             item = input("Enter product name you want to remove: ").lower()
#             my_list.remove(item)
#         elif digit == 6:  # add a product to list
#             item = input("Enter product name you want to add: ").lower()
#             my_list.append(item)
#         elif digit == 7:  # print illegal items
#             for item in my_list:
#                 if len(item) < 3 or not item.isalpha():
#                     print(item)
#         elif digit == 8:  # remove duplicates from list
#             my_list = list(dict.fromkeys(my_list))
#         # end of switch
#
#         digit = int(input("Enter a digit between 1-9: "))
#
#
# shopping("Milk,Cottage,Tomatoes,Milk,DY")


#7.2.7
# def arrow(my_char, max_length):
#     for i in range(max_length):
#         for j in range(i):
#             print(my_char, end="")
#         print("\r")
#     for i in range(max_length):
#         for j in range(max_length - i):
#             print(my_char, end="")
#         print("\r")
#
# arrow('*', 5)

