from xml.dom import minidom


def XML():
    print('\nЗадание 4: XML Теги')
    xmldoc = minidom.parse('currency.xml')
    Tags1 = xmldoc.getElementsByTagName('CharCode')
    Tags2 = xmldoc.getElementsByTagName('Nominal')

    counter = 0
    print('Словарь:')
    for _ in Tags1:
        print('CharCode: ', Tags1[counter].firstChild.data, 'Nominal: ', Tags2[counter].firstChild.data)
        counter += 1
