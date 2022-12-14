import view


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
    match menu_number:
        case 1:
            view.show_all()
        case 2:
            view.search_menu()
        case 3:
            view.edit_menu()
        case 4:
            view.delete_menu()
        case 5:
            view.file_menu()
        case 0:
            quit()


def get_search_data():
    obj = input('Введите данные для поиска: ')
    return obj
