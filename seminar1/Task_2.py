#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# - 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

list = []

#Создаем список в цикле
for i in range(0, 5):
    list.append(int(input("Введите число: ")))

#Нулевой вариант, используем функцию "max"
#print(max(list))  


max = list[0]


#Первый вариант:
# for i in range(1, 5):
#     if list[i] > max:
#         max = list[i]


# print(max)

 

#Второй вариант поиска/ В этом варианте нельзя изменять i-й элемент списка 
for i in list:
    if i > max:
        max = i

print(max)

#Третий вариант через функции
def array(m):
    x = []
    for i in range(m):
        a = int(input(f'Введите x{i + 1}: '))
        x.append(a)
    
    return x

def max_el(array):
    
    maxim = 0

    for i in range(len(array)):
        if array[i] > array[maxim]:
            maxim = i

    return array[maxim]

l = int(input('Введите количество элементов: '))
new_array = array(l)
maxim = max_el(new_array)
print(f'Максимальный элемент: {maxim}')
