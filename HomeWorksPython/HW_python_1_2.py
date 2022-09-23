# Напишите программу для
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


list_x = [0, 1]
list_y = [0, 1]
list_z = [0, 1]

for x in list_x:
    for y in list_y:
        for z in list_z:
            if(not(x or y or z)) == (not x and not y and not z):
                print(f"Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - Истинно, при X ={x} , Y={y}, Z={z}")

print("Второй вариант")

for x in range(2):
    for y in range(2):
        for z in range(2):
            if(not(x or y or z)) == (not x and not y and not z):
                print(f"Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - Истинно, при X ={x} , Y={y}, Z={z}")

print("Третий вариант")

list_xyz = [[0, 0, 0],
[0, 0, 1],
[0, 1, 0],
[0, 1, 1],
[1, 0, 0],
[1, 0, 1],
[1, 1, 0],
[1, 1, 1]]



for i in range(0, len(list_xyz)):
    if (not(list_xyz[i][0] or list_xyz[i][1] or list_xyz[i][2])) == (not list_xyz[i][0] and not list_xyz[i][1] and not list_xyz[i][2]):
        print(f"Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - Истинно, при X ={list_xyz[i][0]} , Y={list_xyz[i][1]}, Z={list_xyz[i][2]}")
    else:
        print("False")
