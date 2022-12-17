# Делает Женя
# - Просмотр всего списка
#  - Поиск элемента
#  - Добавление элемента
#  - Удаление элемента
def output_data(data: list) -> None:  # output is list of contacts
    if len(data) > 0:
        print("-"*105+'\n')
        for contact in data:
            while len(contact) < 5:
                contact.append('-')
            print(contact[0].center(20), '|'.center(1), contact[1].center(20), '|'.center(1),
                  contact[2].center(20), '|'.center(
                      1), contact[3].center(15), '|'.center(1), contact[4].center(16), '|'.center(1) + '\n')
            print("-"*105+'\n')
    else:
        print('PhoneBook is empty')


output_data([['qwer', 'ewq', '1234569'],['', 'fdsa', '987654']])


def find_contact():
    pass
