# Напишите программу, которая выводит текст:
#
# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."

# str_ = '''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."'''
# print(str_)

# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
#
# «Hello [введенное имя] [введенная фамилия]! You just delved into Python».

# name = input()
# family = input()
#
# print('Hello ' + name + ' ' + family + '!' + ' You just delved into Python')

# Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
#
# «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

team = input()
team_len = len(team)
print('Футбольная команда ' + team + ' имеет длину ' + str(team_len) + ' символов')