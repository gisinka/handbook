import os.path
import re
from record import Record


def main():
    while True:
        if choose_action() == -1:
            break


def choose_action():
    print('Комманды:', end='\n')
    print('Создать справочник - 1', end='\n')
    print('Сменить справочник - 2', end='\n')
    print('Добавить запись - 3', end='\n')
    print('Изменить запись - 4', end='\n')
    print('Найти запись - 5', end='\n')
    print('Удалить запись - 6', end='\n')
    print('Выйти - 0', end='\n')
    command = int(input())
    if command == 1:
        create_handbook()
    elif command == 2:
        select_handbook()
    elif command == 3:
        add()
    elif command == 4:
        change_record()
    elif command == 5:
        search()
    elif command == 6:
        remove_record()
    elif command == 0:
        return -1


def create_handbook():
    global currentHandbook
    handbook_name = input("Введите имя справочника: ")
    if os.path.exists(os.path.abspath(handbook_name + '.hdb')):
        print('Справочник с таким именем уже существует.', end='\n')
        return
    currentHandbook = handbook_name
    handbook = open(f"{handbook_name}.hdb", "a")
    handbook.close()
    print('Справочник создан.', end='\n')


def select_handbook():
    global currentHandbook
    handbook_name = input("Введите имя нужного справочника: ")
    if os.path.exists(os.path.abspath(handbook_name + '.hdb')):
        currentHandbook = handbook_name
        print('Текущий справочник изменён.', end='\n')
    else:
        print('Справочника с таким именем не существует. Создать его? (y/n)', end='\n')
        answer = input()
        if answer == 'y':
            currentHandbook = handbook_name
            handbook = open(f"{handbook_name}.hdb", "a")
            handbook.close()
            print('Справочник создан.', end='\n')
        if answer == 'n':
            return


def add():
    global currentHandbook
    print('Введите через пробел имя, фамилию, номер телефона, город и e-mail:', end='\n')
    input_str = input()
    records, storage = read_handbook()
    if validate_record(input_str):
        new_item = Record(input_str)
        if new_item.email not in records:
            storage.append(new_item)
    for items in storage:
        handbook = open(f'{currentHandbook}.hdb', 'a')
        handbook.write(items.__str__() + '\n')
        handbook.close()


def change_record():
    print('Введите e-mail изменяемой записи:', end='\n')
    email = input()
    records, storage = read_handbook()
    for item in storage:
        if item.email == email:
            print('Введите новые параметры записи:', end='\n')
            new_record = input()
            if validate_record(new_record) and new_record not in records:
                storage.remove(item)
                storage.append(Record(new_record))
    for item in storage:
        handbook = open(f'{currentHandbook}.hdb', 'a')
        handbook.write(item.__str__() + '\n')
        handbook.close()


def read_handbook():
    storage = []
    handbook = open(f'{currentHandbook}.hdb', 'r')
    records = handbook.readlines()
    handbook.close()
    for record in records:
        if validate_record(record):
            storage.append(Record(record))
    return records, storage


def search():
    global currentHandbook
    print('Введите один из параметров для поиска:', end='\n')
    searching_param = input()
    records, storage = read_handbook()
    counter = 0
    for item in storage:
        if item.__contains__(searching_param):
            print(item.__str__(), end='\n')
            counter += 1
    print('Найдено записей: ', counter, end='\n')


def remove_record():
    global currentHandbook
    print('Введите e-mail удаляемой записи:', end='\n')
    email = input()
    records, storage = read_handbook()
    for item in storage:
        if item.email == email:
            storage.remove(item)
            print('Запись удалена.', end='\n')
        handbook = open(f'{currentHandbook}.hdb', 'a')
        handbook.write(item.__str__() + '\n')
        handbook.close()



def validate_record(record):
    fields = record.split(' ')
    if len(fields) != 5:
        return False
    is_correct_name = bool(re.match(r"[А-Я][а-я]+", fields[0]))
    is_correct_surname = bool(re.match(r"[А-Я][а-я]+", fields[1]))
    is_correct_number = bool(re.match(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", fields[2]))
    is_correct_city = bool(re.match(r"^[а-яА-Я\- ]+$", fields[3]))
    is_correct_email = bool(re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", fields[4]))
    return is_correct_name and is_correct_surname and is_correct_number and is_correct_city and is_correct_email


currentHandbook = ''
main()
