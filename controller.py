import view


def click():
    view.main_menu()


def op_choice():
    while True:
        op = input('-> ')
        if not (op in '1234560'):
            print('Нет такой операции, попробуйте снова!')
            continue
        return op
        break