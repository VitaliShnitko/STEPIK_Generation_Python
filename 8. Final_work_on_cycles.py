#8 Final work on cycles

# На обработку поступает натуральное число.
# Нужно написать программу, которая выводит на экран сумму чётных цифр этого числа или 0,
# если чётных цифр в записи нет. Программист торопился и написал программу неправильно.
#
# Найдите все ошибки в этой программе
# (их может быть одна или несколько).
# Известно, что каждая ошибка затрагивает только одну строку и
# может быть исправлена без изменения других строк.

# n = int(input())
# s = 0
# while n > 1:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)


# На обработку поступает последовательность из 8 целых чисел.
# Известно, что вводимые числа по абсолютной величине не превышают 10^12 .
# Нужно написать программу, которая выводит на экран количество делящихся нацело на 4
# чисел в исходной последовательности и максимальное делящееся нацело на 4 число.
# Если делящихся нацело на 4 чисел нет, требуется на экран вывести «NO».
# Программист торопился и написал программу неправильно.
#
# Найдите все ошибки в этой программе (их может быть одна или несколько).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.

# n = 8
# count = 0
# maximum = -10**12
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


# Дано натуральное число n ,(n>99).
# Напишите программу, которая определяет его третью (с начала) цифру.

# n = int(input())
# count = 0
# while n > 99:
#     b = n % 10
#     count = b
#     n //= 10
# print(count)


# На обработку поступает последовательность из 4 целых чисел.
# Известно, что вводимые числа по абсолютной величине не превышают 10^8.
# Нужно написать программу, которая выводит на экран количество нечётных чисел
# в исходной последовательности и максимальное нечётное число. Если нечётных чисел нет,
# требуется на экран вывести «NO». Программист торопился и написал программу неправильно.
#
# Найдите все ошибки в этой программе (их может быть одна или несколько).
# Известно, что каждая ошибка затрагивает только одну строку
# и может быть исправлена без изменения других строк.

# n = 4
# count = 0
# maximum = -10**8
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


# На вход программе подается натуральное число n.
# Напишите программу, которая печатает звездную рамку размерами n×19.

# n = int(input())
# print('*'*19)
# for i in range(n-2):
#     print('*' + ' ' * 17 + '*')
# print('*'*19)


# Дано натуральное число. Напишите программу, которая вычисляет:
#
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи
# (если цифр больших семи нет, то вывести 1,если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

n = int(input())
count_sum_5 = 0
count_3 = 0
counter_last = n % 10
couter_last_digit = 0
count_7 = 1
count_0_5 = 0
count_chet = 0
while n != 0:
    a = n % 10
    if a == 3:
        count_3 += 1
    if a == counter_last:
        couter_last_digit += 1
    if a %2 == 0:
        count_chet += 1
    if a > 5:
        count_sum_5 += a
    if a > 7 :
        count_7 *= a
    if a in (0, 5):
        count_0_5 += 1
    n //= 10
print(count_3)
print(couter_last_digit)
print(count_chet)
print(count_sum_5)
print(count_7)
print(count_0_5)



