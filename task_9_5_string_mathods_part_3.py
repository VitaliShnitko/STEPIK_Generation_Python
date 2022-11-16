# Дополните приведенный код, используя форматирование строк с помощью метода format,
# так чтобы он вывел текст:
# «In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).


# s = 'In {0}, someone paid {1} {2} for two pizzas.'
# year = '2010'
# summa = '10k'
# cripta = 'Bitcoin'
# print(f"In {year}, someone paid {summa} {cripta} for two pizzas.")


# Дополните приведенный код, используя форматирование строк с помощью f-строк, так чтобы он вывел текст:
# «In 2010, someone paid 10K Bitcoin for two pizzas.» (без кавычек).

year = 2010
amount = '10K'
currency = 'Bitcoin'

print(f'In {year}, someone paid {amount} {currency} for two pizzas.')