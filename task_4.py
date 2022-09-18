# При регистрации на сайтах требуется вводить пароль дважды.
# Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.
#
# Напишите программу, которая сравнивает пароль и его подтверждение.
# Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».

# password = input()
# password_confirm = input()
#
# if password == password_confirm:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# Напишите программу, которая определяет, является число четным или нечетным.

# num = int(input())
#
# if num % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# Напишите программу, которая проверяет,
# что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.

# num = int(input())
#
# digit1 = num // 1000
# digit2 = (num // 100) % 10
# digit3 = (num // 10) % 10
# digit4 = num % 10
#
# if digit1 + digit4 == digit2 - digit3:
#     print('ДА')
# else:
#     print('НЕТ')


# Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.

# age = int(input())
#
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещён')


# Напишите программу, которая определяет,
# являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.


# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# if (num2 - num1) + num2 == num3:
#     print('YES')
# else:
#     print('NO')


# Напишите программу, которая определяет наименьшее из двух чисел.

num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1)
else:
    print(num2)

