import json

class Employee:
    def __init__(self, id, name, rank, salary):
        self.id = id
        self.name = name
        self.rank = rank
        self.salary = salary
        
        
    def __str__(self):
        return f'id: {self.id}; ФИО: {self.name}'
    
    def to_list_employee(self):
        return [self.id, self.name, self.rank, self.salary]

    def to_JSON(self):
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys=True)
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'rank': self.rank, 'salary': self.salary}
    
    
class J_Employee(Employee):
    def __init__(self, dict_employee: dict):
        self.id = dict_employee['id']
        self.name = dict_employee['name']
        self.rank = dict_employee['rank']
        self.salary = dict_employee['salary']
    