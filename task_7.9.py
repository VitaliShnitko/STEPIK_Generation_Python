# Дано натуральное число n. Напишите программу,
# которая печатает численный треугольник с высотой равной n, в соответствии с примером.

# num = 1
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(num, end=' ')
#         num += 1
#     print()


# Дано натуральное число n. Напишите программу,
# которая печатает численный треугольник с высотой равной n, в соответствии с примером:
#
# 1
# 121
# 12321
# 1234321
# 123454321

# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     for k in range(i-1, 0, -1):
#         print(k, end='')
#     print()


# На вход программе подается два натуральных числа a и b (a< b).
# Напишите программу, которая находит натуральное
# число из отрезка [a;b] с максимальной суммой делителей.

a = int(input())
b = int(input())
summ_count = 0
summ_x = 0
for x in range(a, b+1):
    count = 0
    for i in range(1, b+1):
        if x % i == 0:
            count += i
        if count >= summ_count:
            summ_count = count
            summ_x = x
print(summ_x, summ_count)




