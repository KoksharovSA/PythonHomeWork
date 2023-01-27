import json

class Person:
    def __init__(self, id, name, phone_number):
        self.id = id
        self.name = name
        self.phone_number = phone_number

        
        
    def __str__(self):
        return f'id: {self.id}\n ФИО: {self.name}\n Номер телефона: {self.phone_number}\n'
    
    def to_list_person(self):
        return [self.id, self.name, self.phone_number]

    def to_JSON(self):
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys=True)
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'phone_number': self.phone_number}
    
    
class J_Person(Person):
    def __init__(self, dict_employee: dict):
        self.id = dict_employee['id']
        self.name = dict_employee['name']
        self.phone_number = dict_employee['phone_number']
    