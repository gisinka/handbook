import os.path

from storage import *


def main():
    select_handbook()
    while True:
        if choose_action() == -1:
            break


def choose_action():
    global currentHandbook
    print('Комманды:', end='\n')
    print('Создать справочник - 1', end='\n')
    print('Сменить справочник - 2', end='\n')
    print('Добавить запись - 3', end='\n')
    print('Изменить запись - 4', end='\n')
    print('Найти запись - 5', end='\n')
    print('Удалить запись - 6', end='\n')
    print('Вывести содержимое справочника - 7', end='\n')
    print('Выйти - 0', end='\n')
    command = int(input())
    if command == 1:
        create_handbook()
    elif command == 2:
        select_handbook()
    elif command == 3:
        currentHandbook.add_record()
    elif command == 4:
        currentHandbook.change_record()
    elif command == 5:
        currentHandbook.search_records()
    elif command == 6:
        currentHandbook.remove_record()
    elif command == 7:
        currentHandbook.print_storage()
    elif command == 0:
        if currentHandbook is not None:
            currentHandbook.save_on_disk()
        return -1


def create_handbook():
    global currentHandbook
    handbook_name = input("Введите имя нового справочника: ")
    if os.path.exists(os.path.abspath(handbook_name + '.hdb')):
        print('Справочник с таким именем уже существует.', end='\n')
    currentHandbook = Storage(handbook_name)
    print('Справочник выбран в качестве текущего.', end='\n')


def select_handbook():
    global currentHandbook
    handbook_name = input("Введите имя справочника для выбора: ")
    if os.path.exists(os.path.abspath(handbook_name + '.hdb')):
        if currentHandbook is not None:
            currentHandbook.save_on_disk()
        currentHandbook = Storage(handbook_name)
        print('Текущий справочник изменён.', end='\n')
    else:
        print('Справочника с таким именем не существует. Создать его? (y/n)', end='\n')
        if input() == 'y':
            if currentHandbook is not None:
                currentHandbook.save_on_disk()
            currentHandbook = Storage(handbook_name)
            print('Справочник создан.', end='\n')
        else:
            select_handbook()


currentHandbook = None
main()
