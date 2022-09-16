# Геометрической прогрессией называется последовательность чисел b_1, b_2,...., b_n , каждое из которых, начиная с b_2 ,
# получается из предыдущего умножением на одно и то же постоянное число qq (знаменатель прогрессии), то есть
#
# b_n=b_{n−1}* q
#
# Если известен первый член прогрессии и её знаменатель, то n-ый член геометрической прогрессии находится по формуле
#
# b_n=b_1* q^{n-1}


# b_1 = int(input())
# q = int(input())
# n = int(input())
#
# b_n = b_1 * (q**(n-1))
#
# print(b_n)

# Напишите программу, которая находит полное число метров по заданному числу сантиметров.

# amount_sm = int(input())
# count_met = amount_sm // 100
# print(count_met)

# n школьников делят k мандаринов поровну,
# неделящийся остаток остается в корзине.
# Сколько целых мандаринов достанется каждому школьнику?
# Сколько целых мандаринов останется в корзине?

amount_schoolboy = int(input())
amount_mandarin = int(input())

count_mandarin = amount_mandarin // amount_schoolboy
remainder_mandarin = amount_mandarin % amount_schoolboy
print(count_mandarin)
print(remainder_mandarin)






