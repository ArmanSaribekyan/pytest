documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def pers_docum(numbers):
    for docum_number in documents:
        if docum_number["number"] == numbers:
            print(f'{docum_number["name"]} - владелец документа с номером'
                  f' {docum_number["number"]}\n')
            return True
    else:
        print('Номер документа не найден.\n')
        return False


def shelf_number(numbers):
    for direct in directories.items():
        for docum_number in direct[1]:
            if docum_number == numbers:
                print(f'"{numbers}" лежит на полке {direct[0]}.\n')
                return True
    else:
        print(f'Документа "{numbers}" не существует.\n')
        return False


def list_doc():
    for i, doc in enumerate(documents, 1):
        print(f'{i}. {doc["type"]} "{doc["number"]}" "{doc["name"]}"')
    print('Это все документы, которые у нас есть.\n')
    return True


def add_doc(type_doc, number, name, direct_number):
    if direct_number in directories.keys():
        documents.append({"type": type_doc, "number": number, "name": name})
        directories[direct_number].append(number)
        print(f'Документ добавлен на {direct_number} полку.\n')
        return True
    else:
        print('Такой полки не существует.\n')
    return False


def main():
    while True:
        user_input = input('Инфо - "?"\nВведите команду: ')
        if user_input == 'p':
           pers_docum(input('Введите номер документа: '))
        elif user_input == 's':
            shelf_number(input('Введите номер документа: '))
        elif user_input == 'l':
            list_doc()
        elif user_input == 'a':
            add_doc(input('Введите тип документа: '),
                    input('Введите номер документа: '),
                    input('Введите имя владельца документа: '),
                    input('Введите номер полки: '))
        elif user_input == '?':
            print('p – по номеру документа узнать владельца;\n'
                  's – номер полки, на которой хранится документ;\n'
                  'l – все документы;\n'
                  'a – добавляем новый документ;\n'
                  'e - выход из программы.\n')
        elif user_input == 'e':
            print('До свидания!')
            return
        else:
            print('Некорректная команда.\n')


if __name__ == '__main__':
    main()
