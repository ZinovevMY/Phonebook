import view


def click():
    view.main_menu()


def get_op_choice():
    while True:
        op = input('-> ')
        if not (op in '1234560'):
            print('Нет такой операции, попробуйте снова!')
            continue
        return op
        break


def get_search_data():
    obj = input('Введите фамилию или номер абонента (если ничего не вводить, будет выдан весь справочник): ')
    return obj
