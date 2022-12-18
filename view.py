import menu_struct as ms
import db_operations as dbo
import controller as contr
import keyboard as kb


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
        print('PhoneBook is empty')
    return 'sa', 0


def get_menu_choice(options_number: int):
    while True:
        op = int(input('-> '))
        if not (op in range(0, options_number)):
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
        case 5:
            submenu_name, submenu_opt_count = ms.file_menu()
        case 0:
            quit()
    return submenu_name, submenu_opt_count


def show_all_menu_navigation():
    all_list, all_list_sep = dbo.read_data('phonebook.txt')
    show_all(all_list)
    while True:
        if kb.is_pressed('0'):
            break


def search_menu_navigation(menu_number: int):
    if menu_number == 1:
        search_obj = get_search_data()
        dbo.read_data('phonebook.txt', search_obj)
    elif menu_number == 0:
        contr.click()


def edit_menu_navigation(menu_number: int):
    if menu_number == 1:
        search_obj = get_search_data()
        dbo.write_data('phonebook.txt', search_obj)
    elif menu_number == 2:
        search_obj = get_search_data()
        dbo.edit_data('phonebook.txt', search_obj)
    elif menu_number == 0:
        contr.click()


def delete_menu_navigation(menu_number: int):
    if menu_number == 1:
        search_obj = get_search_data()
        dbo.delete_object('phonebook.txt', search_obj)
    elif menu_number == 0:
        contr.click()


def get_search_data():
    obj = input('Введите данные абонента: ')
    return obj


def get_contact_details():
    while True:
        print("Введите ФИО абонента, а также номер телефона и примечание."
              "Данные вводите через пробел, либо через разделитель (, ; : *) без пробелов!")
        details = input('->')
        if details == '':
            print()

