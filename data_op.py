import view as v


def find_contact(data: list, find_el: str) -> list:
    result = []
    for contact in data:
        for el in contact:
            if find_el in el:
                result.append(contact)
    if not (len(result)):
        result.append(None)
    return result


def add_contact() -> list:
    data = []
    tmp_data = []
    i = 0
    while i < 5:
        match i:
            case 0:
                tmp = input('Фамилия: ')
            case 1:
                tmp = input('Имя: ')
            case 2:
                tmp = input('Отчество: ')
            case 3:
                tmp = input('Телефон: ')
            case 4:
                tmp = input('Примечание: ')
        if (',' not in tmp) and (':' not in tmp) and (';' not in tmp) and ('*' not in tmp):
            if len(tmp_data) > 0:
                tmp_data.append(tmp)
            i += 1
        print('ошибка повторите ввод')
    data.append(tmp_data)
    if len(data) > 0:
       return data
    else:
       print("Нечего добавлять!")
       return None


def del_contact(data: list) -> list:
    find_el = input("Введите данные о контакте для удаления: ")
    del_list = find_contact(data, find_el)
    if del_list is None:
        print("Нечего удалять!")
    elif len(del_list) == 1:
        return data.remove(del_list)
    else:
        v.show_all(del_list)
        del_num = int(input("Введите порядкой номер элемента (сверху вниз от 1) для удаления: ")) - 1
        del_list = del_list[del_num]
        return data.remove(del_list)
