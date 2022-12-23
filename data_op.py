import view as v
import db_operations as dbo


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
            if len(tmp):
                tmp_data.append(tmp)
                i += 1
            else:
                tmp = '-'
                tmp_data.append(tmp)
                i += 1
    data.append(tmp_data)
    if len(data) > 0:
        return data
    else:
        print("Нечего добавлять!")
        return None


def del_contact(data: list) -> list:
    v.show_all(data)
    while True:
        try:
            n = int(
                input('введите порядковый номер контакта для удаления (c единицы): '))
        except ValueError:
            print(f'введите число от 1 до {len(data)}: ')
        else:
            if (n > 0) and (n < len(data)+1):
                del data[n-1]
                return data
  

def edit_data(file: str, find_el: str) -> None:
    data, sep = dbo.read_data(file)
    tmp = find_contact(data, find_el)
    v.show_all(tmp)
    if None in tmp:
        return
    while True:
        try:
            n = int(
                input('введите порядковый номер контакта для изменения (c единицы): '))
        except ValueError:
            print(f'введите число от 1 до {len(tmp)}: ')
        else:
            if (n > 0) and (n < len(tmp)+1):
                tmp = tmp[n-1]
                break
    new_tmp = add_contact()
    index_ = data.index(tmp)
    if None in new_tmp:
        print('нечего менять')
    else:
        data[index_] = new_tmp[0]
        dbo.write_data(data, sep, command=1)
