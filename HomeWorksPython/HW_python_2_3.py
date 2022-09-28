# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input("Введите число: "))

numberKit = []
suma = 0
sumAnother = 0

for i in range(1, n + 1):
    number = round((1+1/i)**i) #если брать пример из презентации
    #number = (1+1/i)**i       #если оставлять чистые вычисления
    numberKit.append(number)
    suma = suma + number
    
print(numberKit)
print(suma)