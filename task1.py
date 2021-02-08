"""
    Вводится строка.
    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

string = input('Введите строку: ')
amount = 0

for char in string:
    if not char.isalpha():
        amount += 1
print('Количество слов:', amount + 1)    

count = 0
for i in string.split():
    if len(i) > count:
        count = len(i)
        word = i
print(f'Самое длинное слово: {word}. Его длина: {len(word)}')