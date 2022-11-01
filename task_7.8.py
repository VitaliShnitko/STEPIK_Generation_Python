# Дано натуральное число n (n≤ 9).
# Напишите программу, которая печатает таблицу размером n×3
# состоящую из данного числа (числа отделены одним пробелом).

# n = int(input())
# for i in range(n):
#     for j in range(3):
#             print(n, end=' ')
#     print()


# Дано натуральное число (n≤ 9). Напишите программу, которая печатает таблицу размером n×5,
# где в i-ой строке указано число i (числа отделены одним пробелом).

# n = int(input())
# for i in range(1, n+1):
#     for j in range(5):
#             print(i, end=' ')
#     print()


# Дано натуральное число n (n≤ 9).
# Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n в соответствии с примером.

# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i+j)
#     print()


# Дано нечетное натуральное число n.
# Напишите программу, которая печатает равнобедренный звездный треугольник с основанием,
# равным n в соответствии с примером:
# *
# **
# ***
# ****
# ***
# **
# *

# n = int(input())
# for i in range(n//2 + 1):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
# for i in range(n//2, 0, -1):
#     for j in range(i, 0, -1):
#         print('*', end='')
#     print()



# Дано натуральное число n. Напишите программу,
# которая печатает численный треугольник в соответствии с примером:
# 1
# 22
# 333
# 4444
# 55555
# ...

# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i, end='')
#     print()


# Имеется 100100 рублей. Сколько быков, коров и телят можно купить на все эти деньги,
# если плата за быка – 10 рублей, за корову – 5 рублей,
# за теленка – 0.5 рубля и надо купить 100 голов скота?

# for b in range(1, 11):
#     for k in range(1, 21):
#         for t in range(1, 201):
#             if b * 10 + k * 5 + t * 0.5 == 100 and b + k + t == 100:
#                 print(b, k, t)


# Решите уравнение в натуральных числах 28n + 30k + 31m = 365.

# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print(n, k, m)


# В 1769 году Леонард Эйлер сформулировал обобщенную версию Великой теоремы Ферма,
# предполагая, что по крайней мере n энных степеней необходимо для получения суммы,
# которая сама является энной степенью для n > 2. Напишите программу для опровержения гипотезы Эйлера
# (продержавшейся до 1967 года), и найдите четыре положительных целых числа,
# сумма 5-х степеней которых равна 5-й степени другого положительного целого числа.
#
# Таким образом, найдите пять натуральных чисел a,b,c,d,e удовлетворяющих условию:
# a^5+b^5+c^5+d^5=e^5.
# В ответе укажите сумму a+b+c+d+e.

for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                summ = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(summ ** 0.2)
                if summ == e ** 5:
                    print(a + b + c + d + e)
                    break










