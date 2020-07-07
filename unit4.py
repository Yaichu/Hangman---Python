letter = input("Enter a letter: ")
if len(letter) > 1:
    if not letter.isalpha():
        print("E3")
    else:
        print("E1")
elif not letter.isalpha():
    print("E2")
else:
    print(letter.lower())


#4.2.2
# word = input("Enter a word: ")
# if word == word[::-1]:
#     print("OK")
# else:
#     print("NOT")


#4.2.3
# temp = input("Insert the temperature you would like to convert:")
# temp_num = int(temp[:-1])
# temp_last = temp[-1]
# far = (9 * temp_num + (32 * 5)) / 5
# cel = (5 * temp_num - 160) / 9
# if temp_last.lower() == "f":
#     print(cel)
# elif temp_last.lower() == "c":
#     print(far)


#4.2.4
# import datetime
# import calendar
# date = input("Enter a date: ")
# date_to_weekday = datetime.datetime.strptime(date, '%d/%m/%Y').weekday()
# print(calendar.day_name[date_to_weekday])