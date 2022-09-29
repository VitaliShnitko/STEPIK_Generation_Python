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

# team = input()
# team_len = len(team)
# print('Футбольная команда ' + team + ' имеет длину ' + str(team_len) + ' символов')

# Даны названия трех городов. Напишите программу,
# которая определяет самое короткое и самое длинное название города.

# city1 = input()
# city2 = input()
# city3 = input()
#
# len1 = len(city1)
# len2 = len(city2)
# len3 = len(city3)
#
# if len1 == min(len(city1), len(city2), len(city3)):
#     print(city1)
# elif len2 == min(len(city1), len(city2), len(city3)):
#     print(city2)
# else:
#     print(city3)
# if len1 == max(len(city1), len(city2), len(city3)):
#     print(city1)
# elif len2 == max(len(city1), len(city2), len(city3)):
#     print(city2)
# else:
#     print(city3)

# Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет можно ли из длин этих строк
# построить возрастающую арифметическую прогрессию.

# str1 = len(input())
# str2 = len(input())
# str3 = len(input())
#
# if (2 * str2 - str3 - str1) * (2 * str3 - str2 - str1) * (2 * str1 - str2 - 3) == 0:
#     print('YES')
# else:
#     print('NO')

# Напишите программу, которая считывает одну строку,
# после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.

str1 = input()
s = 'синий'
if s in str1:
    print('YES')
else:
    print('NO')