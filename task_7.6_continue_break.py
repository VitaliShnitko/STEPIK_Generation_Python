# На вход программе подается число n > 1.
# Напишите программу, которая выводит его наименьший отличный от 1 делитель.

# n = int(input())
#
# for i in range(2, n+1):
#     if n % i == 0:
#         print(i)
#         break


# На вход программе подается натуральное число n. Напишите программу,
# которая выводит числа от 1 до n включительно за исключением:
# чисел от 5 до 9 включительно;
# чисел от 17 до 37 включительно;
# чисел от 78 до 87 включительно.


n = int(input())

for i in range(1, n+1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)


