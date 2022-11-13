# Дополните приведенный код, используя срезы,
# так чтобы он вывел первые 12 символов строки s.

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[:12])


# Дополните приведенный код, используя срезы,
# так чтобы он вывел последние 9 символов строки s.

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])


# Дополните приведенный код, используя срезы,
# так чтобы он вывел каждый 7 символ строки s начиная от начала строки.

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::7])


# Дополните приведенный код, используя срезы,
# так чтобы он вывел строку s в обратном порядке.

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])


# На вход программе подается одно слово, записанное в нижнем регистре.
# Напишите программу, которая определяет является ли оно палиндромом.

# text = input()
# if text[::] == text[::-1]:
#     print('YES')
# else:
#     print('NO')


# На вход программе подается одна строка. Напишите программу, которая выводит:
#
# общее количество символов в строке;
# исходную строку повторенную 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удаленным первым и последним символом.

text = input()
len_text = len(text)
text_x3 = text*3
first_symbol_text = text[:1]
first_3_symbol_text = text[:3]
last_3_symbol = text[-3:]
revers_text = text[::-1]
del_first_last_symbol_text = text[1:-1]

print(len_text, text_x3, first_symbol_text, first_3_symbol_text,
      last_3_symbol, revers_text, del_first_last_symbol_text, sep='\n')





