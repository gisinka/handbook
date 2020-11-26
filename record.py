import re


class Record(object):

    def __init__(self, record):
        fields = record.split(' ')
        self.name = fields[0]
        self.surname = fields[1]
        self.number = fields[2]
        self.city = fields[3]
        self.email = fields[4]

    def __str__(self):
        return f'{self.name} {self.surname} {self.number} {self.city} {self.email}'

    def __contains__(self, item):
        return item in self.name or item in self.surname or item in self.number or item in self.city or item in self.email

    @staticmethod
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
