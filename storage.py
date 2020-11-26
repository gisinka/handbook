import os

from record import *


class Storage(object):
    def __init__(self, handbook_name):
        self.storage = []
        self.name = handbook_name
        if not os.path.exists(os.path.abspath(handbook_name + '.hdb')):
            handbook = open(f"{handbook_name}.hdb", "a")
            handbook.close()
        handbook = open(f'{self.name}.hdb', 'r')
        records = handbook.readlines()
        handbook.close()
        for record in records:
            if Record.validate_record(record):
                self.storage.append(Record(record))

    def change_record(self):
        print('Введите e-mail изменяемой записи:', end='\n')
        email = input()
        for item in self.storage:
            if item.email == email:
                print('Введите новые параметры записи:', end='\n')
                input_str = input()
                if Record.validate_record(input_str):
                    new_record = Record(input_str)
                    if new_record not in self.storage:
                        self.storage.remove(item)
                        self.storage.append(new_record)
                        break

    def add_record(self):
        print('Введите через пробел имя, фамилию, номер телефона, город и e-mail:', end='\n')
        input_str = input()
        if Record.validate_record(input_str):
            new_record = Record(input_str)
            if new_record not in self.storage:
                self.storage.append(new_record)
        else:
            print('Введенная запись неверна', end='\n')

    def search_records(self):
        print('Введите один из параметров для поиска:', end='\n')
        searching_param = input()
        counter = 0
        for item in self.storage:
            if item.__contains__(searching_param):
                print(item.__str__(), end='\n')
                counter += 1
        print('Найдено записей: ', counter, end='\n')

    def remove_record(self):
        print('Введите e-mail удаляемой записи:', end='\n')
        email = input()
        for item in self.storage:
            if item.email == email:
                self.storage.remove(item)
                print('Запись удалена.', end='\n')
                break

    def save_on_disk(self):
        handbook = open(f'{self.name}.hdb', 'w')
        for item in self.storage:
            handbook.write(item.__str__() + '\n')
        handbook.close()

    def print_storage(self):
        for item in self.storage:
            print(item.__str__(), end='\n')

    @staticmethod
    def create_handbook(handbook_name):
        handbook = open(f"{handbook_name}.hdb", "a")
        handbook.close()

