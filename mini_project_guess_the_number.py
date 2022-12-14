# Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100
# и просит пользователя угадать это число. Если догадка пользователя больше случайного числа,
# то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
# Если догадка меньше случайного числа, то программа должна
# вывести сообщение 'Слишком мало, попробуйте еще раз'.
# Если пользователь угадывает число, то программа должна
# поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.





# Тимур загадал число от 1 до n.
# За какое наименьшее количество вопросов (на которые Тимур отвечает "больше" или "меньше")
# Руслан может гарантированно угадать число Тимура?
from random import randint

# 1 решение
n = int(input())
count = 0
while n != 1:
    if n % 2 != 0:
        n += 1
    n //= 2
    count += 1
print(count)

# 2 решение
from math import log2, ceil
print (ceil(log2(int(input()))))