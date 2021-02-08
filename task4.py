# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'


# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53


# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6


# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)


# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'

string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'
string = string.replace(', ', ' ')
print(string)
print(string.rindex('s'))
print(string.count('I') + string.count('i'))
string.find('simply dummy text')
print(string[15:32])
(len(string))
print(string[:29] * 3 + string[29:])
