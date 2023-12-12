import re
from first_task import database


def year(date):
    delimiters = " |\\."
    result = re.split(delimiters, date)
    return result[2]


def authors():
    print('Задание 2: Поиск книг по автору')
    Years = ['2015', '2018']
    author = input('Введите имя автора: ')

    for i in database:
        if author in i[4] and (year(i[6]) in Years):
            print(i)
    print('\n')
