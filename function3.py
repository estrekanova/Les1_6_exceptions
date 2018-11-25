documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
    {'type': 'diploma', 'number': '12К-12342'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people_search():
    number = input('Введите номер документа:')
    name = ''
    for document in documents:
        if document['number'] == number:
            name = document['name']
            break
    return name


def people_list_print():
    for document in documents:
        print('{} "{}" "{}"'.format(document['type'], document['number'], document['name']))


def search_shelf():
    number = input('Введите номер документа:')
    shelf_number = ''
    for directory, numbers in directories.items():
        if numbers.count(number) > 0:
            shelf_number = directory
        break
    return shelf_number


def add_document():
    document_type = input('Введите тип документа: ')
    document_number = input('Введите номер документа:')
    name = input('Введите владельца документа: ')
    shelf_number = input('Введите номер полки: ')

    documents.append({'type': document_type, 'number': document_number, 'name': name})

    if shelf_number not in directories.keys():
        directories[shelf_number] = list()
    directories[shelf_number].append(document_number)

    return document_number


def add_shelf():
    shelf_number = input('Введите номер полки: ')
    if shelf_number not in directories.keys():
        directories[shelf_number] = list()
    return directories[shelf_number]


def delete_document():
    document_number = input('Введите номер документа:')
    for document in documents:
        if document['number'] == document_number:
            documents.remove(document)
        break
    for shelf, documents_list in directories.items():
        if documents_list.count(document_number)>0:
            directories[shelf].remove(document_number)
        break


def move_document():
    document_number = input('Введите номер документа:')
    shelf_number = input('Введите номер полки:')
    for shelf, documents_list in directories.items():
        if documents_list.count(document_number)>0:
            directories[shelf].remove(document_number)
            break
    if shelf_number not in directories.keys():
        directories[shelf_number] = list()
    directories[shelf_number].append(document_number)
    return [document_number, shelf_number]


# Задание 3 к лекции 1_6
def print_names():
    for document in documents:
        try:
            print(document['name'])
        except KeyError:
            print(f'Нет ключа "name" для документа №{document["number"]}')


print_names()

# while True:
#     command = input('\nВведите код команды. Для выхода введите "e": ')
#
#     if command.lower() == 'e':
#         break
#
#     if command.lower() == 'p':
#         name = people_search()
#         if name == '':
#             print('Документ отсутствует в списке')
#         else:
#             print('Владелец документа: {}'.format(name))
#         continue
#
#     if command.lower() == 'l':
#         people_list_print()
#         continue
#
#     if command.lower() == 's':
#         shelf_number = search_shelf()
#         if shelf_number == '':
#             print('Документ отсутствует в списке')
#         else:
#             print('Документ находитсяна полке №{}'.format(shelf_number))
#         continue
#
#     if command.lower() == 'a':
#         print('Документ %s добавлен в список'%add_document())
#         print(documents,'\n')
#         print(directories)
#         continue
#
#     if command.lower() == 'd':
#         delete_document()
#         print(documents)
#         print(directories)
#         continue
#
#     if command.lower() == 'as':
#         add_shelf()
#         print(documents)
#         print(directories)
#         continue
#
#     if command.lower() == 'm':
#         document_info = move_document()
#         print('Документ №"{}" перемещен на полку {}'.format(document_info[0], document_info[1]))
#         print(documents)
#         print(directories)
#         continue
