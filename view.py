import menu_struct as ms
import db_operations as dbo
import controller as contr
import keyboard as kb
import data_op as dop

FILE_TYPE = 0 # Переменная отвечает за то, с каким файлом (txt или csv) будем работать


def show_all(data: list):
    if None in data:
        print('контакт не существует')
    elif len(data) > 0:
        print("-" * 105 + '\n')
        for contact in data:
            while len(contact) < 5:
                contact.append('-')
            print(contact[0].center(20), '|'.center(1), contact[1].center(20), '|'.center(1),
                  contact[2].center(20), '|'.center(
                1), contact[3].center(15), '|'.center(1), contact[4].center(16), '|'.center(1) + '\n')
            print("-" * 105 + '\n')
    else:
        print('Справочник пуст')
    return 'sa', 0


def get_menu_choice(options_number: int):
    while True:
        op = int(input('-> '))
        if not (0 <= op <= options_number):
            print('Нет такой операции, попробуйте снова!')
            continue
        return op


def submenus_navigation(menu_number: int):
    submenu_opt_count = 0
    submenu_name = ''
    match menu_number:
        case 1:
            submenu_name, submenu_opt_count = ms.show_all_menu()
        case 2:
            submenu_name, submenu_opt_count = ms.search_menu()
        case 3:
            submenu_name, submenu_opt_count = ms.edit_menu()
        case 4:
            submenu_name, submenu_opt_count = ms.delete_menu()
        case 0:
            quit()
    return submenu_name, submenu_opt_count


def show_all_menu_navigation():
    if FILE_TYPE == 1:
        all_list, all_list_sep = dbo.read_data('phonebook.txt')
    else:
        all_list, all_list_sep = dbo.read_data('phonebook.csv')
    show_all(all_list)
    while True:
        if kb.is_pressed('0'):
            break


def search_menu_navigation(menu_number: int):
    if FILE_TYPE == 1:
        file = 'phonebook.txt'
    else:
        file = 'phonebook.csv'
    if menu_number == 1:
        search_obj = get_search_data()
        search_list, search_sep = dbo.read_data(file)
        result = dop.find_contact(search_list, search_obj)
        show_all(result)
        print('Для выхода нажмите 0.\n')
        while True:
            if kb.is_pressed('0'):
                break
    elif menu_number == 0:
        contr.click()


def edit_menu_navigation(menu_number: int):
    if FILE_TYPE == 1:
        file = 'phonebook.txt'
    else:
        file = 'phonebook.csv'
    if menu_number == 1:
        contact_list = dop.add_contact()
        dbo.write_data(contact_list)
    elif menu_number == 2:
        search_obj = get_search_data()
        dop.edit_data(file, search_obj)
    elif menu_number == 0:
        contr.click()


def delete_menu_navigation(menu_number: int):
    if FILE_TYPE == 1:
        file = 'phonebook.txt'
    else:
        file = 'phonebook.csv'
    if menu_number == 1:
        search_list, search_sep = dbo.read_data(file)
        result = dop.del_contact(search_list)
        dbo.write_data(result, search_sep, 1)
    elif menu_number == 0:
        contr.click()


def get_search_data():
    obj = input('Введите данные абонента: ')
    return obj
