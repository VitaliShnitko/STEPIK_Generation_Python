# Напишите функцию get_middle_point(x1, y1, x2, y2),
# которая принимает в качестве аргументов координаты
# концов отрезка (x_1, y_1)(x) и (x_2, y_2)(x) и
# возвращает координаты точки являющейся серединой данного отрезка.

# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     a = (x1+x2) / 2
#     b = (y1+y2) / 2
#     return a, b
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# Напишите функцию get_circle(radius),
# которая принимает в качестве аргумента радиус
# окружности и возвращает два значения:
# длину окружности и площадь круга, ограниченного данной окружностью.


import math
# объявление функции
def get_circle(radius):
    c = 2 * math.pi * radius
    s = math.pi * (radius ** 2)
    return c, s

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)