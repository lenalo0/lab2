import random
from first_task import database
from second_task import year


def list_of_books():
    print('Задание 3: Генератор библеографических ссылок')
    new_file = open('Books.txt', 'w+')
    Title_base = []
    print('Список книг:')
    for i in range(20):
        x = random.randint(0, len(database) - 1)
        while database[x][1] in Title_base:
            x = random.randint(0, len(database) - 1)
        else:
            Title_base.append(database[x][1])
        print(f'{str(i + 1)} | {database[x][1]}')
        new_file.write(f'{str(i + 1)} | {database[x][3]} | {database[x][1]} | {year(database[x][6])}\n')
    print('Перенесён в файл Books.txt')
    new_file.close()
