class Record(object):

    def __init__(self, record):
        fields = record.split(' ')
        self.name = fields[0]
        self.surname = fields[1]
        self.number = fields[2]
        self.city = fields[3]
        self.email = fields[4]

    @property
    def __str__(self):
        return f'{self.name} {self.surname} {self.number} {self.city} {self.email}'

    def __contains__(self, item):
        return item in self.name or item in self.surname or item in self.number or item in self.city or item in self.email
