# Описание проекта:
# требуется написать программу, способную шифровать и дешифровать текст
# в соответствии с алгоритмом Цезаря.
# Она должна запрашивать у пользователя следующие данные:
#
# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).

# Задаем четыре вопроса пользователю: шифр-дешифр, язык, шаг, текст.
# За каждым вопросом стоит while-проверка, что введенный ответ является корректным значением.

whats_direction = input('Что мы должны сделать: шифровать или дешифровать? \n').lower()
while whats_direction != 'шифровать' and whats_direction != 'дешифровать':
    whats_direction = input('Что-то не то ты ввёл. Напиши "шифровать" либо "дешифровать". \n').lower()

whats_language = input('Какой нужен язык: русский или английский? \n').lower()
while whats_language != 'русский' and whats_language != 'английский':
    whats_language = input('Что-то не то ты ввёл. Напиши "русский" либо "английский". \n').lower()

whats_step = input('На сколько символовов мы сдвигаем буквы по алфавиту? Ответ напиши числом. \n')
while whats_step.isdigit() != True:
    whats_step = input('Что-то не то ты ввёл. Напиши число. \n')

whats_text = input('Какой текст нужно использовать сейчас? \n')
while whats_text.isspace() == True:
    whats_text = input('Что-то не то ты ввёл. Введи текст. \n')


# Объявляем функцию с четырьмя аргументами – соответственно четырем вопросам.
def caesar(direction, language, step, text):
    # Четыре словаря под русские и английские символы, большие и маленькие.
    # В теории можно обойтись без них и обращаться к таблице Unicode.
    # Но мне было удобнее создать свои словари.

    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    # Объявляем цикл for. Количество итераций равно длине строки text.
    for i in range(len(text)):

        # Задаем локальные переменные: длину алфавита и значения словарей.
        if language == 'русский':
            alphas = 32
            low_alphabet = lower_rus_alphabet
            upp_alphabet = upper_rus_alphabet
        if language == 'английский':
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alphabet = upper_eng_alphabet

        # Если text[i] является буквой:
        if text[i].isalpha():

            # Находим место символа text[i] в словаре upp_alphabet либо low_alphabet.
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])

            # Если нужно дешифровать, то:
            if direction == 'дешифровать':
                # Находим индекс для измененного символа.
                # Новый ндекс = Старый индекс - Шаг % Длина алфавита
                index = (place - int(step)) % alphas


            # Если нужно зашифровать, то:
            elif direction == 'шифровать':
                # Находим индекс для измененного символа.
                # Новый индекс = Старый индекс + Шаг % Длина алфавита
                index = (place + int(step)) % alphas

            # Выводим измененный символ.
            if text[i] == text[i].lower():
                print(low_alphabet[index], end='')
            if text[i] == text[i].upper():
                print(upp_alphabet[index], end='')

                # Если text[i] не является буквой:
        else:
            # Делаем print этого символа без изменений.
            print(text[i], end='')


# Вызываем функцию, передавая в аргументы четыре input`а из начала кода.
caesar(whats_direction, whats_language, whats_step, whats_text)

s = "Hawnj pk swhg xabkna ukq nqj."
d = 'abcdefghijklmnopqrstuvwxyz'
for k in range(25):
    b = ''
    for i in range(len(s)):
        if not s[i].isalpha():
            b += s[i]
        else:
            if s[i].isupper():
                b += (d[d.find(s[i].lower())-k]).upper()
            else:
                b += d[d.find(s[i].lower())-k]
    print(b)


# На вход программе подается строка текста на английском языке,
# в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра
# Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.

alphavit_engB = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphavit_engM = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

li = input().split()
itog = ''
for i in li:
   z = 0
   for j in i:
       if j.isalpha() == True:
           z += 1
   for j in i:
       mestoB = alphavit_engB.find(j)            #АВЕ, ЦЕЗАРЬ
       mestoM = alphavit_engM.find(j)
       new_mestoB = mestoB + z
       new_mestoM = mestoM + z
       if j.isalpha() == True:
           if j == j.upper():
               itog += alphavit_engB[new_mestoB]
           elif j == j.lower():
               itog += alphavit_engM[new_mestoM]
       else:
           itog += j
   itog += ' '
print(itog)











