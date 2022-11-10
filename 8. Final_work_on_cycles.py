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

n = 8
count = 0
maximum = -10**12
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')






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
# maximum = 999
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = i
#             break
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


