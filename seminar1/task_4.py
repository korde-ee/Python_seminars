# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:* 
# 6,78 -> 7
# 5 -> нет
#  0,34 -> 3


num = float(input("Введите число: "))

part_num = int(num *10 % 10)

if num % 1 == 0:
    print("Нет дробной части")
else:
    print(part_num)