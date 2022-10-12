# Даны два целых числа m и n ( m ≤ n). Напишите программу,
# которая выводит все числа от m до n включительно.

# m = int(input())
# n = int(input())
#
# for i in range(m, n+1):
#     print(i)

# Даны два целых числа mm и nn. Напишите программу,
# которая выводит все числа от m до n включительно в порядке возрастания, если m < n,
# или в порядке убывания в противном случае.

m = int(input())
n = int(input())

if m < n:
    for i in range(m, n+1):
        print(i)
elif m > n:
    for i in range(m, n-1, -1):
        print(i)
else:
    print(m)
