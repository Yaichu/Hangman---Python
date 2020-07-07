from collections import OrderedDict
def choose_word(file_path, index):
    with open(file_path, "r") as input_file:
        file_content = input_file.read()
    # print(file_content)

    nodup = " ".join(OrderedDict.fromkeys(file_content.split()))  # new content without duplicates - with order
    # print(len(nodup.split()))  # number of different words in the string
    # print(nodup.split())  # list
    # print(nodup)

    word = file_content.split()[index % len(file_content.split()) - 1]
    # print(word)
    return len(nodup.split()), word


print(choose_word(r"C:\Users\yael\PycharmProjects\hangman\words.txt", 3))

##9.1.1

# def are_files_equal(file1, file2):
#     with open(file1, "r") as input_file1:
#         file_content1 = input_file1.read()
#     with open(file2, "r") as input_file2:
#         file_content2 = input_file2.read()
#     if file_content1 == file_content2:
#         return True
#     else:
#         return False
#
#
# print(are_files_equal(r"C:\Users\yael\PycharmProjects\hangman\yael.txt", r"C:\Users\yael\PycharmProjects\hangman\danny.txt"))



## 9.1.2
#
# # sampleFile = input("Enter a file path: ")
# sampleFile = r"C:\Users\yael\PycharmProjects\hangman\sampleFile.txt"
# with open(sampleFile, "r") as input_sampleFile:
#         file_content1 = input_sampleFile.read()
#
# task = input("Enter a task: ")
# if task == "sort":
#     list_content = list(file_content1.split(" "))
#     # print(list_content)
#     list_content = list(dict.fromkeys(list_content))
#     list_content.sort()
#     print(list_content)
# elif task == "rev":
#     rev_list = list(file_content1.split("\n"))
#     new_list = []
#     for row in rev_list:
#         rev_row = row[::-1]
#         new_list.append(rev_row)
#     merged_string = '\n'.join(new_list)
#     print(merged_string)
#     # reversed_content = file_content1[::-1]
#     # print(reversed_content)
# elif task == "last":
#     num = int(input("Enter a number: "))
#     list_content = file_content1.split("\n")
#     start_row = len(list_content) - num
#     for i in range(len(list_content) - 1, start_row - 1, -1):
#         print(list_content[i])

# #9.2.2
#
# def copy_file_content(source, destination):
#     with open(source, "r") as input_source:
#          copy_content = input_source.read()
#     with open(destination, "w") as input_dest:
#          input_dest.write(copy_content)
#     # with open(destination, "r") as input_dest:
#     #      print(input_dest.read())
#
#
# copy_file_content(r"C:\Users\yael\PycharmProjects\hangman\copy.txt", r"C:\Users\yael\PycharmProjects\hangman\paste.txt")

# #9.2.3
# def who_is_missing(file_name):
#     with open(file_name, "r") as input_file:
#         file_content = input_file.read()
#     no_commas = file_content.split(",")
#     sorted_content = sorted(no_commas)
#     for i in range(len(sorted_content) - 1):
#         if int(sorted_content[i + 1]) - int(sorted_content[i]) > 1:
#             missing_num = int(sorted_content[i]) + 1
#     with open("found.txt", "w") as input_dest:
#         input_dest.write(str(missing_num))
#     return missing_num
#
#
# print(who_is_missing(r"C:\Users\yael\PycharmProjects\hangman\findMe.txt"))

# #9.3.1
#
# def my_mp3_playlist(file_path):
#     with open(file_path, "r") as input_file:
#         file_content = input_file.read()
#     new_list = file_content.split("\n")
#
#     splittt_list = []
#     for elem in new_list:
#         splittt_list.append(elem.split(";"))
#
#     max = 0
#     singers = []
#
#     for i in range(len(splittt_list)):
#         singers.append(splittt_list[i][1])
#         song_len = splittt_list[i][2]
#         song_float = float(song_len.replace(":", "."))
#         if song_float > max:
#             max = song_float
#             longest_song = splittt_list[i][0]
#
#     count = 0
#     best_singer = ""
#     for singer in singers:
#         curr_freq = singers.count(singer)
#         if curr_freq > count:
#             count = curr_freq
#             best_singer = singer
#
#     num_of_songs = len(splittt_list)
#     return longest_song, num_of_songs, best_singer
#
#
# print(my_mp3_playlist("songs.txt"))

# #9.3.2
# def my_mp4_playlist(file_path, new_song):
#     with open(file_path, "r") as input_file:
#         file_content = input_file.read()
#     new_list = file_content.split("\n")
#
#     splittt_list = []
#     for elem in new_list:
#         splittt_list.append(elem.split(";"))
#     splittt_list[2][0] = new_song
#     print(splittt_list)
#
#
# print(my_mp4_playlist("songs.txt", "Python Love Story"))
