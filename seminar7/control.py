import view
import multy
import sum
import div
import diff
import log

def button_click():
    value_a = view.getValue() # Метод получения значений из view
    value_b = view.getValue()
    operationName = view.getOperationName() # получение знака операции (*, /, +, -)
    result = getOperation(value_a, value_b, operationName) # Инициализируем входные данные нашей модели
    view.view(result, operationName, value_a, value_b) # возвращаем результат, имя операции и переменные
    log.log(result, operationName, value_a, value_b)


def getOperation(value_a, value_b, operationName):
    match operationName:
        case '+':
            sum.init(value_a, value_b)
            return sum.operation()
        case '-':
            diff.init(value_a, value_b)
            return diff.operation()
        case '/':
            div.init(value_a, value_b)
            return div.operation()
        case '*':
            multy.init(value_a, value_b)
            return multy.operation()
        