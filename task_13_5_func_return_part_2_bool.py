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
# def is_prime(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:  # если исходное число делится на какое-либо отличное от 1 и самого себя
#             flag = False
#     if num == 1:
#         return False
#     elif flag == True:
#         return  True
#     else:
#         return False
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))


# Напишите функцию is_one_away(word1, word2),
# которая принимает в качестве аргументов два слова word1 и word2
# и возвращает значение True если слова имеют одинаковую длину
# и отличаются ровно в 1 символе и False в противном случае.

# # объявление функции
# def is_one_away(word1, word2):
#     count = 0
#     if len(word1) == len(word2):
#         for i in range(0, len(word1)):
#             if word1[i] == word2[i]:
#                 count += 1
#         if len(word1) - count == 1:
#             return True
#         else:
#             return False
#
#     else:
#         return False
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))


# Напишите функцию is_palindrome(text),
# которая принимает в качестве аргумента строку text и
# возвращает значение True если указанный текст является
# палиндромом и False в противном случае.

# 1способ решения
def is_palindrome(text):
    if text.lower() == text[::-1].lower():
        return True
    else:
        text1 = "".join(i for i in text if i.isalpha())
        if text1.lower() == text1[::-1].lower():
            return True
        else:
            return False
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

# 2способ решения
# объявление функции
def is_palindrome(text):
    text = [i.lower() for i in text if i.isalpha()]
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))