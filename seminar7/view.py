def view(data, operationName, value_a, value_b):
    print(f"Результат {value_a} {operationName} {value_b} = {data}")
    
def getValue():
    return int(input("Введите значение аргумента: "))

def getOperationName():
    return input("Введите операцию: ")