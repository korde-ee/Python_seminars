# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
from fileinput import close
import random
from re import M

n = int(input("Введите число: "))

list = []

for i in range(n):
    list.append(random.randint(-n,n))
    
print(list)

#file = open('d:\\Разработчик\\Python\\HomeWorksPython\\file.txt','r')

file = open('file.txt','r')

position = []
for line in file:
    #print(line)
    position.append(line)
firstPos = int(position[0])
secondPos = int(position[1])

if firstPos > n and secondPos > n:
    print(f"Значение позиций из файла больше длинны списка")
elif firstPos <= n and secondPos > n:
    print(f"Значение второго числа больше длинны списка")
    multy = list[firstPos - 1]
    print(multy)
elif firstPos > n and secondPos <= n:
    print(f"Значение первого числа больше длинны списка")
    multy = list[secondPos - 1]
    print(multy)
elif firstPos <= n and secondPos <= n: 
    multy = list[firstPos - 1] * list[secondPos - 1]
    print(multy)

file = close()