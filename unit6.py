def is_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if is_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    old_letters_print = sorted(old_letters_guessed)
    old_letters_print = " -> ".join(old_letters_print)
    print(old_letters_print)
    return False


letter = input("Enter a letter: ").lower()
old_letters = ['a', 'p', 'c', 'f']
print(try_update_letter_guessed(letter, old_letters))

#6.1.2
# def shift_left(my_list):
#     new_list = []
#     new_list.append(my_list[1])
#     new_list.append(my_list[2])
#     new_list.append(my_list[0])
#     return new_list
#     # another optional solution
#     # temp = my_list[0]
#     # my_list[0] = my_list[1]
#     # my_list[1] = my_list[2]
#     # my_list[2] = temp
#     # return my_list
#
# print(shift_left(['monkey', 2.0, 1]))

#6.2.3
# def format_list(my_list):
#     even_list = (my_list[::2])
#     new_string = ', '.join(even_list) + " and " + my_list[-1]
#     return new_string
#
#
# print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))

#6.2.4
# def extend_list_x(list_x, list_y):
#     # list_y.append(list_x)
#     list_x[:0] = list_y
#     return list_x
#
#
# print(extend_list_x([4, 5, 6], [1, 2, 3]))

#6.3.1
import collections
# def are_lists_equal(list1, list2):
#     # option 1
#     # if collections.Counter(list1) == collections.Counter(list2):
#     # option 2
#     if sorted(list1) == sorted(list2):
#         return True
#     return False
#
#
# print(are_lists_equal([0.6, 1, 2, 3], [3, 2, 0.6, 1]))

#6.3.2
# def longest(my_list):
#     return max(my_list, key=len)
#
#
# print(longest(["111", "234", "2000", "goru", "birthday", "09"]))
