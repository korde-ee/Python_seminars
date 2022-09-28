# Реализуйте алгоритм перемешивания списка.

import random

n = int(input("Введите длину списка: "))

listMy = []

for i in range(n):
    listMy.append(random.randint(0, n + 7))
    
print(listMy)

def perestanovka(list):
    for i in range(len(list)):
        indexMix = random.randint(0, n-1)
        temp = list[indexMix]
        list[indexMix] = list[i]
        list[i] = temp
    return list

print(perestanovka(listMy))