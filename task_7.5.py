# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.

# num = int(input())
#
# while num != 0:
#     last_digit = num % 10
#     print(last_digit)
#     num = num // 10


# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

# num = int(input())
#
# while num != 0:
#     last_digit = num % 10
#     print(last_digit, end='')
#     num = num // 10


# Дано натуральное число n,(n≥10). Напишите программу,
# которая определяет его максимальную и минимальную цифры.
# 1 способ
# num = int(input())
#
# string = str(num)
# max_num = max(string)
# min_num = min(string)
# print('Максимальная цифра равно', max_num)
# print('Минимальная цифра равно', min_num)

# 2 способ

num = int(input())
min_num = 9
max_num = 0

while num != 0:
    if num % 10 < min_num:
        min_num = num % 10
    if num % 10 > max_num:
        max_num = num % 10
    num = num // 10
print('Максимальная цифра равна', max_num)
print('Минимальная цифра равна', min_num)