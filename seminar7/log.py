import datetime
from encodings import utf_8

path = 'log.txt'

def log(data, operationName, value_a, value_b):
    string = f'{datetime.datetime.now()}: {value_a} {operationName} {value_b} = {data}'
    with open(path, 'a', encoding='utf_8') as data:
        data.write(f'{string}\n')

        