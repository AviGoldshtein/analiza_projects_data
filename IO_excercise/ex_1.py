############ q2
# content = ["Hello world",
#            "It’s the first exercise in I/O",
#            "That mean it is number 1",
#            "Not 2",
#            "Not three",
#            "It is exciting",
#            "And i am all 4 it"]
# with open("my_text.txt", mode="w", encoding="utf-8") as file:
#     for line in content:
#         file.write(line + "\n")
import csv

############# q3
# with open("my_text.txt", mode="r", encoding="utf-8") as file:
#     for line in file.readlines():
#         if [num for num in line if num.isnumeric()]:
#             print(line)

############# q4
# with open("my_text.txt", mode="r", encoding="utf-8") as file:
#     num_of_lines = 0
#     num_of_words = 0
#     num_of_words_no_numbers = 0
#     num_of_chars = 0
#     most_frequency_word = {}
#     for line in file.readlines():
#         num_of_lines += 1
#         num_of_words += len(line.split())
#         for word in line.split():
#             if not word.isnumeric():
#                 num_of_words_no_numbers += 1
#
#             num_of_chars += len(word)
#
#             if not word in most_frequency_word:
#                 most_frequency_word[word] = 0
#             most_frequency_word[word] += 1
# most = 0
# word = ""
# for key, val in most_frequency_word.items():
#     if val > most:
#         most = val
#         word = key
#
# print(f"the number of lines: {num_of_lines}")
# print(f"the number of words: {num_of_words}")
# print(f"the number of chars: {num_of_chars}")
# print(f"This word: ~{word}~ appears most often. It appears {most} times")

############# q5
# with (open("my_text.txt", mode="r", encoding="utf-8") as f_reading,
#       open("summary.txt", mode="w", encoding="utf-8") as f_writing):
#     for line in f_reading.readlines():
#         f_writing.write(f"{line[:-1]}, ({len(line.split())}) words\n")

############# q7
# with open("sample_names.csv", mode="r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     first_row_printed = False
#     for row in reader:
#         if first_row_printed:
#             print(f"my name is: {row[0]}, i live in {row[4]}, i work in {row[3]}.")
#         first_row_printed = True

############# q8
# def add_person(name, age, address):
#     with open("myCsv.csv", mode="a", newline='', encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow((name, age, address))
# add_person("Moshe", 25, "har sinay")

############# q9
# all_cities = {}
# with (open("sample_names.csv", mode="r", encoding="utf-8") as reading_file,
#     open("city_summary.csv", mode="w", newline='', encoding="utf-8") as writing_file):
#     reader = csv.reader(reading_file)
#     content_list = list(reader)
#     first_line = content_list[0]
#
#     #reading
#     for row in content_list[1:]:
#         if not row[4] in all_cities: #city init
#             all_cities[row[4]] = {}
#         if not row[2] in all_cities[row[4]]: #title init
#             all_cities[row[4]][row[2]] = 0
#         all_cities[row[4]][row[2]] += 1     #increase one in this city for this title
#
#     #writing
#     writer = csv.writer(writing_file)
#     writer.writerow(("city", "subject" ,"count"))
#     for city, subject_and_count in all_cities.items():
#         for subject, count in subject_and_count.items():
#             writer.writerow((city, subject, count))

############# q10
# import json
# all_poeple = []
# with (open("sample_names.csv", mode="r", encoding="utf-8") as reading_file,
#       open("people.json", mode="w", encoding="utf-8") as writing_file):
#     reader = csv.reader(reading_file)
#     for row in list(reader)[1:]:
#         person = {"first_name": row[0],
#                   "gender": row[1],
#                   "title": row[2],
#                   "Occupation": row[3],
#                   "City": row[4]}
#         all_poeple.append(person)
#
#     json.dump(all_poeple, writing_file, indent=4)

############ q11
# import json
# cities = {}
# with open("people.json", mode="r", encoding="utf-8") as file:
#     content = json.load(file)
#     for person in content:
#         # city = person[""]
#         print(person)
