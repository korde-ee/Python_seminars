# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc
from collections import Counter

list = "aaaaaaabbbbbbccccccccc"
print(f"Исходная строка для сжатия: {list}")
dict = Counter(list)
dict = sorted(dict.items())
# print(sorted(dict.items())) 
print(f"Проверяем через словарь: {dict}")

def coding(list):
    # Объявляем переменную, куда будем сохранять сжатую строку
    encoding = "" 
    
    i = 0
    while i < len(list):
        # подсчитываем количество вхождений символа в индексе `i`
        count = 1
    
        while i + 1 < len(list) and list[i] == list[i + 1]:
            count = count + 1
            i = i + 1
    
        # добавляем к результату текущий символ и его количество
        encoding += str(count) + list[i]
        i = i + 1
    return encoding    

print(f"Сжатая строка: {coding(list)}")


# listDecod = "11a3b7c"
listDecod = input("Введите строку для декодировки: ")

def deCoding(data): 
    decode = '' 
    count = '' 
    for i in data: 
        if i.isdigit(): # Если символ - число. То добавляем его значение в count
            count += i 
        else:  # Если символ не число, тогда повторяем его count раз. И "обнуляем" count
            decode += i * int(count) 
            count = '' 
    return decode

print(f"Раскрытая строка: {deCoding(listDecod)}")