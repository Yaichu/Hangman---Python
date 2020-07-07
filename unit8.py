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



print_hangman(7)




#8.2.1
# data = ("self", "py", 1.543)
# format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"
# print(format_string % data)

#8.2.2
# # from operator import itemgetter
#
# def myfn(x):
#     return x[1]
#
# def sort_prices(list_of_tuples):
#     # list_sorted = sorted(list_of_tuples, key=itemgetter(1), reverse=True)  # key=lambda x: x[1]
#     list_sorted = sorted(list_of_tuples, key=myfn, reverse=True)
#     return list_sorted
#
#
# products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
# print(sort_prices(products))


#8.2.3
# import itertools
# def mult_tuple(tuple1, tuple2):
#     mixed_tuple = tuple(itertools.product(tuple1, tuple2))
#     flup = tuple(itertools.product(tuple2, tuple1))
#     return mixed_tuple + flup
#
#     # Danny's option for learning
#     # list = []
#     # for i in range(len(tuple1)):
#     #     for j in range(len(tuple2)):
#     #         print((tuple1[i], tuple2[j]))
#     #         list.append((tuple1[i], tuple2[j]))
#     # for i in range(len(tuple2)):
#     #     for j in range(len(tuple1)):
#     #         list.append((tuple2[i], tuple1[j]))
#     # return tuple(list)
#
#
# first_tuple = (1, 2)
# second_tuple = (4, 5)
# print(mult_tuple(first_tuple, second_tuple))


#8.2.4
# import itertools
#
# def sort_anagrams(list_of_strings):
#     # wow solution of the internet that we don't fully understand
#     # anagram_list = [list(group) for key, group in itertools.groupby(sorted(list_of_strings, key=sorted), sorted)]
#     # return anagram_list
#
#     # DY's ugly solution but it works and it's ours
#     helper = []
#     anagram_list = []
#     for i in range(len(list_of_strings)):
#         anagram_list.append([])
#         if list_of_strings[i] in helper:
#             continue
#         anagram_list[i].append(list_of_strings[i])
#         for j in range(i + 1, len(list_of_strings)):
#             if sorted(list_of_strings[i]) == sorted(list_of_strings[j]):
#                 anagram_list[i].append(list_of_strings[j])
#                 helper.append(list_of_strings[j])
#     anagram_list = [x for x in anagram_list if x != []]
#     return anagram_list
#
#
# list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
# print(sort_anagrams(list_of_words))


#8.3.2
# import calendar
# from datetime import datetime
# mariah_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}
# digit = int(input("Enter a digit between 1-7: "))
# # my_list = my_str.lower().split(',')
# while digit != 8:
#     # this is a switch on "digit"
#     if digit == 1:  # prints last name
#         print(mariah_dict["last_name"])
#     elif digit == 2:  # prints birth month
#         month_num = int(mariah_dict["birth_date"][3:5])
#         print(calendar.month_name[month_num])
#     elif digit == 3:  # prints number of hobbies
#         print(len(mariah_dict["hobbies"]))
#     elif digit == 4:  # prints last hobby
#         print(mariah_dict["hobbies"][-1])
#     elif digit == 5:  # adds hobby
#         mariah_dict["hobbies"].append("Cooking")
#     elif digit == 6:  # prints full birth date
#         date = mariah_dict["birth_date"]
#         day = int(date[:2])
#         month = int(date[3:5])
#         year = int(date[6:])
#         Tdate = (day, month, year)
#         print(Tdate)
#     elif digit == 7:  # adds age key
#         born = datetime.strptime(mariah_dict["birth_date"], '%d.%m.%Y')
#         today = datetime.today()
#         print(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))
#     # # end of switch
#     #
#     digit = int(input("Enter a digit between 1-8: "))

#8.3.3
#
# def count_chars(my_str):
#     dict = {}
#     for letter in my_str:
#         if letter in dict:
#             dict[letter] += 1
#         else:
#             dict[letter] = 1
#     del dict[" "]
#     return dict
#
#
# magic_str = "abra cadabra"
# print(count_chars(magic_str))


#8.3.4
#
# def inverse_dict(my_dict):
#     new_dict = {}
#     for key, value in my_dict.items():
#         # new_dict[value] = key
#         if value in new_dict.keys():
#             new_dict[value].append(key)
#         else:
#             new_dict[value] = [key]
#     return new_dict
#
#
#
# course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
# print(inverse_dict(course_dict))