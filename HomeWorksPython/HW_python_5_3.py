# Создайте программу для игры в 'Крестики-нолики'.


str1_empty = "        |         |        "
str_line = "________|_________|________"
str_vert_line = "|"
str_2_space = "  "

num1 = '1'
num2 = '2'
num3 = '3'
num4 = '4'
num5 = '5'
num6 = '6'
num7 = '7'
num8 = '8'
num9 = '9'

def printFild():
    print(str1_empty)
    print(str_2_space, num1, str_2_space, str_vert_line, str_2_space, num2, str_2_space, str_vert_line, str_2_space, num3, str_2_space)
    print(str_line)
    print(str1_empty)
    print(str_2_space, num4, str_2_space, str_vert_line, str_2_space, num5, str_2_space, str_vert_line, str_2_space, num6, str_2_space)
    print(str_line)
    print(str1_empty)
    print(str_2_space, num7, str_2_space, str_vert_line, str_2_space, num8, str_2_space, str_vert_line, str_2_space, num9, str_2_space)
    print(str1_empty)

strX = "x"
str0 = "O"

printFild()
count = 0  
for i in range(1, 10):
    
    if i %2 != 0:      
        playerOneCell = input("Игрок 1. Введите номер ячейки: ")
        while playerOneCell == '':
            playerOneCell = input("Игрок 1. Введите номер ячейки: ")
        if playerOneCell == '1':
            if num1 != '1':
                print("Выберите свободную ячейку!")
                playerOneCell = input("Игрок 1. Введите номер ячейки: ")
            else: 
                num1 = strX
                printFild()
        elif playerOneCell == '2':
            if num2 != '2':
                print("Выберите свободную ячейку!")
                playerOneCell = input("Игрок 1. Введите номер ячейки: ")
            else: 
                num2 = strX
                printFild()
        elif playerOneCell == '3':
            if num3 != '3':
                print("Выберите свободную ячейку!")
                playerOneCell = input("Игрок 1. Введите номер ячейки: ")
            else: 
                num3 = strX
                printFild()
        elif playerOneCell == '4':
            if num4 != '4':
                print("Выберите свободную ячейку!")
                playerOneCell = input("Игрок 1. Введите номер ячейки: ")
            else: 
                num4 = strX
                printFild()
        elif playerOneCell == '5':
            if num5 != '5':
                print("Выберите свободную ячейку!")
                playerOneCell = input("Игрок 1. Введите номер ячейки: ")
            else: 
                num5 = strX
                printFild()
        elif playerOneCell == '6':
            if num6 != '6':
                print("Выберите свободную ячейку!")
                playerOneCell = input("Игрок 1. Введите номер ячейки: ")
            else: 
                num6 = strX
                printFild()
        elif playerOneCell == '7':
            if num7 != '7':
                print("Выберите свободную ячейку!")
                playerOneCell = input("Игрок 1. Введите номер ячейки: ")
            else: 
                num7 = strX
                printFild()
        elif playerOneCell == '8':
            if num8 != '8':
                print("Выберите свободную ячейку!")
                playerOneCell = input("Игрок 1. Введите номер ячейки: ")
            else: 
                num8 = strX
                printFild()
        elif playerOneCell == '9':
            if num9 != '9':
                print("Выберите свободную ячейку!")
                playerOneCell = input("Игрок 1. Введите номер ячейки: ")
            else: 
                num9 = strX
                printFild()
        if (num1 == num2 == num3 == strX) or (num4 == num5 == num6 == strX)  or (num7 == num8 == num9 == strX) or (num1 == num5 == num9 == strX) or (num3 == num5 == num7 == strX) or (num1 == num4 == num7 == strX) or (num2 == num5 == num8 == strX) or (num3 == num6 == num9 == strX):
            print("Выиграл игрок 1!")
            break      
    if i %2 == 0:
        playerTwoCell = input("Игрок 2. Введите номер ячейки: ")
        while playerTwoCell == '':
            playerTwoCell = input("Игрок 2. Введите номер ячейки: ")
            
        if playerTwoCell == '1':
            if num1 != '1':
                print("Выберите свободную ячейку!")
            else: 
                num1 = str0
                printFild()
        elif playerTwoCell == '2':
            if num2 != '2':
                print("Выберите свободную ячейку!")
            else: 
                num2 = str0
                printFild()
        elif playerTwoCell == '3':
            if num3 != '3':
                print("Выберите свободную ячейку!")
            else: 
                num3 = str0
                printFild()
        elif playerTwoCell == '4':
            if num4 != '4':
                print("Выберите свободную ячейку!")
            else: 
                num4 = str0
                printFild()
        elif playerTwoCell == '5':
            if num5 != '5':
                print("Выберите свободную ячейку!")
            else: 
                num5 = str0
                printFild()
        elif playerTwoCell == '6':
            if num6 != '6':
                print("Выберите свободную ячейку!")
            else: 
                num6 = str0
                printFild()
        elif playerTwoCell == '7':
            if num7 != '7':
                print("Выберите свободную ячейку!")
            else: 
                num7 = str0
                printFild()
        elif playerTwoCell == '8':
            if num8 != '8':
                print("Выберите свободную ячейку!")
            else: 
                num8 = str0
                printFild()
        elif playerTwoCell == '9':
            if num9 != '9':
                print("Выберите свободную ячейку!")
            else: 
                num9 = str0
                printFild()
        if (num1 == num2 == num3 == str0) or (num4 == num5 == num6 == str0)  or (num7 == num8 == num9 == str0) or (num1 == num5 == num9 == str0) or (num3 == num5 == num7 == str0) or (num1 == num4 == num7 == str0) or (num2 == num5 == num8 == str0) or (num3 == num6 == num9 == str0):
            print("Выиграл игрок 2!")
            break
    count = count + 1
    if count == 9:
        print("Нет победителя")
