def main_menu():
    print('---------------------')
    print('Телефонный справочник')
    print('---------------------')
    print('Выберите действие:\n'
          '1 - Просмотр всего справочника\n'
          '2 - Поиск элемент\n'
          '3 - Добавление/изменение элемента\n'
          '4 - Удаление элемента\n'
          '5 - Загрузка/выгрузка данных \n'
          '0 - Выход')
    return 6


def show_all(data: list):
    if len(data) > 0:
        print("-" * 105 + '\n')
        for contact in data:
            while len(contact) < 5:
                contact.append('-')
            print(contact[0].center(20), '|'.center(1), contact[1].center(20), '|'.center(1),
                  contact[2].center(20), '|'.center(
                    1), contact[3].center(15), '|'.center(1), contact[4].center(16), '|'.center(1) + '\n')
            print("-" * 105 + '\n')
    else:
        print('PhoneBook is empty')
    return 'sa', 0


def search_menu():
    print('--------------')
    print('Поиск абонента')
    print('--------------')
    print('Выберите действие:\n'
          '1 - Поиск\n'
          '0 - Выход')
    return 'sm', 2


def edit_menu():
    print('----------------------')
    print('Работа со справочником')
    print('----------------------')
    print('Выберите действие:\n'
          '1 - Добавление абонента\n'
          '2 - Изменение данных абонента\n'
          '0 - Выход')
    return 'em', 3


def delete_menu():
    print('-----------------')
    print('Удаление абонента')
    print('-----------------')
    print('Выберите действие:\n'
          '1 - Удаление\n'
          '0 - Выход')
    return 'dm', 2


def file_menu():
    print('------------------------')
    print('Загрузка/выгрузка данных')
    print('------------------------')
    print('Выберите действие:\n'
          '1 - Загрузить из файла\n'
          '2 - Выгрузка в файл\n'
          '0 - Выход')
    return 'fm', 3


