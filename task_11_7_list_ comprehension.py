# Дополните приведенный код, используя списочное выражение так,
# чтобы получить новый список,
# содержащий строки исходного списка с удаленным первым символом.

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert',
#             'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
#             'except', 'finally', 'try', 'for', 'from', 'global', 'if',
#             'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#             'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [i[1:] for i in keywords]
# print(new_keywords)


# Дополните приведенный код, используя списочное выражение,
# так чтобы получить новый список, содержащий длины строк исходного списка.

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break',
#             'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
#             'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(keyword) for keyword in keywords]
# print(lengths)

# Дополните приведенный код списочным выражением,
# чтобы получить новый список, содержащий только слова
# длиной не менее пяти символов (включительно).

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break',
#             'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#             'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in',
#             'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [keyword for keyword in keywords if len(keyword) >= 5]
#
# print(new_keywords)


# Дополните приведенный код, используя списочное выражение,
# так чтобы получить список всех чисел палиндромов от 100 до 1000.

# palindromes = [palindrom for palindrom in range(100, 1001) if str(palindrom) == str(palindrom)[::-1]]
#
# print(palindromes)


# На вход программе подается натуральное число n.
# Напишите программу, использующую списочное выражение,
# которая создает список содержащий квадраты чисел от 1 до n
# а затем выводит его элементы построчно, то есть каждый на отдельной строке.

n = int(input())
lst = [i ** 2 for i in range(1, n+1)]
print(*lst, sep='\n')