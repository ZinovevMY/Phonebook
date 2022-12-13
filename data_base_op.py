def read_data(file: str) -> list:
    with open(file, 'r') as f:
        book = f.readlines()
    data = []
    sep = '\n'
    if ',' in book[0]:
        sep = ','
    elif ':' in book[0]:
        sep = ':'
    elif ';' in book[0]:
        sep = ';'
    elif '*' in book[0]:
        sep = '*'
    if sep != '\n':
        for line in book:
            temp = line.strip().split(sep)
            data.append(temp)
    else:
        temp = []
        for line in book:
            if line != '\n':
                temp.append(line.rstrip())
            else:
                data.append(temp)
                temp = []
    data = sorted(data)
    return data


print(read_data('phonebook.csv'))


def write_data(file: str, data: list):

    pass


# Делает Женя
