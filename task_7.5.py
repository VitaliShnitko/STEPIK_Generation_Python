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

# num = int(input())
# min_num = 9
# max_num = 0
#
# while num != 0:
#     if num % 10 < min_num:
#         min_num = num % 10
#     if num % 10 > max_num:
#         max_num = num % 10
#     num = num // 10
# print('Максимальная цифра равна', max_num)
# print('Минимальная цифра равна', min_num)


# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

# num = int(input())
# summa = 0
# count_digits = 0
# multi = 1
# last_digit = num % 10
#
# while num != 0:
#     first_digits = num % 10
#     summa += first_digits
#     count_digits += 1
#     multi *= first_digits
#     sr_arf = summa / count_digits
#     summa_f_l = last_digit + first_digits
#     num = num // 10
# print(summa, count_digits, multi, sr_arf, first_digits, summa_f_l, sep='\n')


# Дано натуральное число n(n > 9). Напишите программу,
# которая определяет его вторую (с начала) цифру.

# num = int(input())
#
# while num > 9:
#     digits = num % 10
#     num = num // 10
# print(digits)


# Дано натуральное число. Напишите программу, которая определяет,
# состоит ли указанное число из одинаковых цифр.
# 1 способ
# num = int(input())
# string = str(num)
# max_digit = max(string)
# min_digit = min(string)
#
# if min_digit == max_digit:
#     print('YES')
# else:
#     print('NO')

# 2 способ
# num = int(input())
# flag = True
# last_digit = num % 10
#
# while num != 0:
#     digit = num % 10
#     if digit != last_digit:
#         flag = False
#     num = num // 10
# if flag == True:
#     print('YES')
# else:
#     print('NO')








