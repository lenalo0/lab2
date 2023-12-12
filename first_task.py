import csv

with open('books.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
counter_i = 0
counter_j = 0

database = [[]]
string = ''

for i in data:
    if len(i) != 1:
        while counter_j < len(i):
            string += i[counter_j]
            counter_j += 1
        i[0] = string
    string = i[0].split(';')
    database[counter_i].extend(string)
    counter_i += 1
    counter_j = 0
    database.append([])
    string = ''

database.pop(len(database) - 1)
csvfile.close()


# List of book titles by condition
def LOBTBK():
    print('Задание 1: Названия')
    counter = 0
    for tag in database:
        if len(tag[1]) > 30:
            counter += 1

    print('Количество книг удовлетворяющих условию: ', counter, '\n')
