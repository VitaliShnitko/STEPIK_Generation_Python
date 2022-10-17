# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.

# num = int(input())
#
# while num != 0:
#     last_digit = num % 10
#     print(last_digit)
#     num = num // 10


# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

num = int(input())

while num != 0:
    last_digit = num % 10
    print(last_digit, end='')
    num = num // 10

