# this function read from *.txt and *.csv format file(data_base)
def read_data(file: str) -> list:
    with open(file, 'r') as data_base:
        book = data_base.readlines()
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
    return data, sep


# this function overwrites the data_base or appends an element to the end depending on the command
def write_data(data: list, sep='\n', command=0) -> None:
    if sep == '\n':
        file = 'phonebook.txt'
        k = 2
    else:
        file = 'phonebook.csv'
        k = 1
    if not command:
        db_com = 'a'  # appends an element to the end
    else:
        db_com = 'w'  # overwrites the data_base
    with open(file, db_com) as data_base:
        for contact in data:
            data_base.write(sep.join(contact))
            data_base.write('\n'*k)


def delete_object(file: str, obj_name: str):
    pass

