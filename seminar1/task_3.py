#1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#Примеры:
#- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

def list_of_numbers(x):
    list = []
    for i in range(-x, x+1):
        list.append(i)
    return list

number = int(input("Введите число: "))

x = list_of_numbers(number)

print(x)



