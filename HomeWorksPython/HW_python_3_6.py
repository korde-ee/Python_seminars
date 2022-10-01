# Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.
import datetime
import time

now = datetime.datetime.now()

# time = now.strftime("%M")

time.time_ns() // 1000000

print(time)


# start = time.monotonic_ns()
# print(start//1000000)
# x=1
# while(x<=100):
#     print(x)
#     x +=1
# finish=time.monotonic_ns()    
# duration = finish -  start
# print(f"That took {duration//1000000}ms")

# x = int(input("Введите начальное значение: "))
# y = int(input("Введите конечное значение: "))
# z = int(input("Введите количество чисел: "))

# list = []

# for j in range(x, y):
#     seed = (j * 73129 + 95121) % 100000
#     list.append(seed)

# for i in range(z):
#     print(list[i] %)


# seconds = time.time() 
# print("Current time in seconds since epoch =", seconds *1000000)

# print(seconds * 1000000 % 1000000)


# seconds = time.time() * 1000000 % 1000000

# print(int(seconds % 10))

n = 45
listOfSeconds = []
x = 10
for i in range(0, n % 10):
    seconds = time.time() * 100000 #% 10000000
    print(seconds)
    
    listOfSeconds.append(int(seconds % x))
    
print(listOfSeconds)
midl = 0
for i in range(len(listOfSeconds)):
    midl = (midl + listOfSeconds[i]) / len(listOfSeconds)

print(midl) 


x = int(input("Введите начальное значение: "))
y = int(input("Введите конечное значение: "))
# z = int(input("Введите количество чисел: "))

def anyDigitList (start, end):
    list = []
    for i in range(start, end + 1):
        list.append(i)
    return list

myList = anyDigitList(x, y)
print(myList)

def myRandomDigit(list, number):
    listOfSeconds = []
    seconds = time.time() * 1000000 % 1000000
    for i in range(0, n):
        listOfSeconds[i].append(seconds(i))
        
    