import view
import db_operations as dbo


def click():
    return view.main_menu()


def get_menu_choice(options_number: int):
    while True:
        op = int(input('-> '))
        if not (op in range(0, options_number)):
            print('Нет такой операции, попробуйте снова!')
            continue
        return op
        break


def submenus_navigation(menu_number: int):
    submenu_opt_count = 0
    submenu_name = ''
    match menu_number:
        case 1:
            submenu_name, submenu_opt_count = view.show_all()
        case 2:
            submenu_name, submenu_opt_count = view.search_menu()
        case 3:
            submenu_name, submenu_opt_count = view.edit_menu()
        case 4:
            submenu_name, submenu_opt_count = view.delete_menu()
        case 5:
            submenu_name, submenu_opt_count = view.file_menu()
        case 0:
            quit()
    return submenu_name, submenu_opt_count


def search_menu_navigation(menu_number: int):
    search_obj = ''
    match menu_number:
        case 1:
            search_obj = get_search_data()
            dbo.read_data('phonebook.txt', search_obj)
        case 2:
            search_obj = get_search_data()
            dbo.read_data('phonebook.txt', search_obj)
        case 0:
            options = click()
            get_menu_choice(options)


def edit_menu_navigation(menu_number: int):
    match menu_number:
        case 1:
            search_obj = get_search_data()
            dbo.write_data('phonebook.txt', search_obj)
        case 2:
            search_obj = get_search_data()
            dbo.edit_data('phonebook.txt', search_obj)
        case 0:
            options = click()
            get_menu_choice(options)


def delete_menu_navigation(menu_number: int):
    match menu_number:
        case 1:
            search_obj = get_search_data()
            dbo.delete_object('phonebook.txt', search_obj)
        case 2:
            search_obj = get_search_data()
            dbo.delete_object('phonebook.txt', search_obj)
        case 0:
            options = click()
            get_menu_choice(options)


def get_search_data():
    obj = input('Введите данные для поиска: ')
    return obj
