
def bd_type_selector():
    print('Выберите тип файла данных для работы:\n'
          '1 - Файл .txt\n'
          '2 - Файл .csv')
    return 2


def main_menu():
    print('---------------------')
    print('Телефонный справочник')
    print('---------------------')
    print('Выберите действие:\n'
          '1 - Просмотр всего справочника\n'
          '2 - Поиск элемент\n'
          '3 - Добавление/изменение элемента\n'
          '4 - Удаление элемента\n'
          '0 - Выход')
    return 5


def show_all_menu():
    print('------------')
    print('Все абоненты')
    print('------------')
    print('Для выхода нажмите цифру 0! ')
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
