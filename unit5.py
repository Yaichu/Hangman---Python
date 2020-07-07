def is_valid_input(letter_guessed):
    if len(letter_guessed) > 1 or not letter_guessed.isalpha():
        return False
    else:
        return True


letter = input("Enter a letter: ")
print(is_valid_input(letter))


#5.3.4
# def last_early(my_str):
#     last_char = my_str[-1]
#     if last_char in my_str[:-1]:
#         return True
#     else:
#         return False
#
#
# string = input("Enter a string: ").lower()
# print(last_early(string))

#5.3.5
# def isClose(n1, n2, n3):
#     if n2 - n1 == 1 or n3 - n1 == 1:
#         return True
#     return False
#
# def isFar(n1, n2, n3):
#     if n3 - n1 >= 2 and n3 - n2 >= 2:
#         return True
#     return False
#
# def distance(num1, num2, num3):
#     n1 = abs(num1)
#     n2 = abs(num2)
#     n3 = abs(num3)
#     if isClose(n1, n2, n3) and (isFar(n1, n2, n3) or isFar(n1, n3, n2)):
#         return True
#     else:
#         return False
#
# print(distance(1, 2, 10))

#5.3.6
# def fix_age(age):
#     if age == 15 or age == 16 or age < 13 or age > 19:
#         return age
#     return 0
#
# def filter_teens(a=13, b=13, c=13):
#     a = fix_age(a)
#     b = fix_age(b)
#     c = fix_age(c)
#     return a + b + c
#
# print(filter_teens(2,15,1))

#5.3.7
# def chocolate_maker(small, big, x):
#     BIG_LENGTH = 5
#     temp = 0
#     if x >= big * BIG_LENGTH:
#         temp = x - big * BIG_LENGTH
#         if small >= temp:
#             return True
#     else:
#         temp = x % BIG_LENGTH
#         if small >= temp:
#             return True
#     return False
# print(chocolate_maker(3, 2, 9))

#5.4.1
# def func(num1, num2):
#     """ :returns sum of 2 numbers
#         :var num1: first number
#         :var num2: second number"""
#
#     sum = num2 + num1
#     return sum
#
# def main():
#     print(func(9, 3))
#
# if __name__ == "__main__":
#     main()
