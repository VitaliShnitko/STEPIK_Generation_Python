# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа, и возвращает значение True
# если существует невырожденный треугольник со
# сторонами side1, side2, side3 и False в противном случае.

# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))


# Напишите функцию is_prime(num),
# которая принимает в качестве аргумента натуральное число
# и возвращает значение True если число является простым и False в противном случае.

# объявление функции
def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:  # если исходное число делится на какое-либо отличное от 1 и самого себя
            flag = False
    if num == 1:
        return False
    elif flag == True:
        return  True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))