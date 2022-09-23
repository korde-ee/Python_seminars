# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def weekend_day(num):
    if num == 1 or num <= 5:
        print("День не выходной")
    elif num == 6 or num == 7:
        print("Это выходной день")

number = int(input("Введите число от 1 до 7: "))
weekend_day(number)