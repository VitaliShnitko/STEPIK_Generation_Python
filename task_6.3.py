# На плоскости евклидово расстояние между двумя точками(x1;y1) b (x2;y2)
# num1 = float(input())
# num2 = float(input())
# num3 = float(input())
# num4 = float(input())
#
# p = ((num1 - num3) ** 2 + (num2 - num4) ** 2) ** 0.5
#
# print(p)

# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
# from math import pi
# r = float(input())
# p = pi
# S = p * (r ** 2)
# C = 2 * p * r
# print(S)
# print(C)

# В математике выделяют следующие средние значения:
#
# среднее арифметическое чисел a и b
# среднее геометрическое чисел a и b
# среднее гармоническое чисел a и b
# среднее квадратичное чисел a и b

# a = float(input())
# b = float(input())
#
# arif = (a + b) / 2
# geo = (a * b) ** 0.5
# gar = (2 * a * b) / (a + b)
# kva = ((a ** 2 + b ** 2) / 2) ** 0.5
# print(arif)
# print(geo)
# print(gar)
# print(kva)

# Напишите программу, вычисляющую значение тригонометрического выражения sin x + cos x + tan^2x
# по заданному числу градусов x.

# from math import sin, cos, tan, radians
# x = radians(float(input()))
#
# trig = sin(x) + cos(x) + (tan(x) ** 2)
# print(trig)

# Напишите программу, вычисляющую значение ⌈x⌉ +⌊x⌋ по заданному вещественному числу x.

# from math import floor, ceil
# x = float(input())
#
# a = ceil(x)
# b = floor(x)
#
# result = a + b
# print(result)

# Даны три вещественных числа a, b, c. Напишите программу,
# которая находит вещественные корни квадратного уравнения
# ax^2 + bx + c = 0.

a = float(input())
b = float(input())
c = float(input())

D = (b ** 2) - (4 * a * c)
if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    if x1 < x2:
        print(x1)
        print(x2)
    else:
        print(x2)
        print(x1)
elif D == 0:
    x = -(b / (2 * a))
    print(x)
else:
    print('Нет корней')





