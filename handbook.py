import os.path
import re


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
    record = input()
    if is_correct_record(record):
        handbook = open(currentHandbook + '.hdb', 'r')
        records = handbook.read()
        handbook.close()
        if record in records:
            print('Такая запись уже существует.', end='\n')
            return
        if record.split(' ')[4] in records:
            print('Запись с таким e-mail уже существует.', end='\n')
            return
        handbook = open(f'{currentHandbook}.hdb', 'a')
        handbook.write(record + '\n')
        handbook.close()
        print('Запись добавлена.', end='\n')
    else:
        print('Неверный ввод. Повторите попытку.')


def change_record():
    print('Введите e-mail изменяемой записи:', end='\n')
    email = input()
    handbook = open(f'{currentHandbook}.hdb', 'r')
    records = handbook.read()
    handbook.seek(0)
    if email in records:
        print('Введите новое значение:', end='\n')
        changed_record = input()
        if is_correct_record(changed_record):
            records = handbook.readlines()
            handbook.close()
            handbook = open(f'{currentHandbook}.hdb', 'w')
            for record in records:
                if email in record:
                    handbook.write(changed_record + '\n')
                else:
                    handbook.write(record + '\n')
            print('Значение изменено.', end='\n')
        else:
            print('Неверный ввод. Повторите попытку.', end='\n')
        return
    print('Такой записи не существует.', end='\b')


def search():
    global currentHandbook
    print('Введите один из параметров для поиска:', end='\n')
    searching_param = input()
    found_records_count = 0
    handbook = open(f'{currentHandbook}.hdb', 'r')
    records = handbook.readlines()
    for record in records:
        if searching_param in record:
            print(record)
            found_records_count += 1
    handbook.close()
    print('Найдено записей: ', found_records_count, end='\n')


def remove_record():
    global currentHandbook
    print('Введите e-mail удаляемой записи:', end='\n')
    email = input()
    handbook = open(f'{currentHandbook}.hdb', 'r')
    records = handbook.readlines()
    handbook.close()
    handbook = open(currentHandbook + '.hdb', 'w')
    is_deleted = False
    for record in records:
        if email not in record:
            handbook.write(record)
        else:
            is_deleted = True
    handbook.close()
    if is_deleted:
        print('Запись удалена.', end='\n')
    else:
        print('Записи с таким e-mail не существует.', end='\n')


def is_correct_record(record):
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
