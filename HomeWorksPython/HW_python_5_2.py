# 2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# вариант человек против человека:
from random import randint

def inputCount(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, cangies):
    print(f"{name} взял {k}, теперь у него {counter} конфет. Осталось в игре {cangies} конфет.")


player1 = "Игрок 1"
player2 = "Игрок 2"
# player1 = input("Игрок 1. Введите имя: ")
# player2 = input("Игрок 2. Введите имя: ")


cangies = 150
# cangies = int(input("Введите количество конфет в игре: "))

flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while cangies > 28:
    if flag:
        k = inputCount(player1)
        counter1 += k
        cangies -= k
        flag = False
        p_print(player1, k, counter1, cangies)
    else:
        k = inputCount(player2)
        counter2 += k
        cangies -= k
        flag = True
        p_print(player2, k, counter2, cangies)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")