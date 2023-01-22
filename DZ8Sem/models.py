

class Employee:
    def __init__(self, id, name, rank, salary):
        self.id = id
        self.name = name
        self.rank = rank
        self.salary = salary
        
    def __str__(self):
        return f'id: {self.id}; ФИО: {self.name}'
    
    def list_employee(self):
        return [self.id, self.name, self.rank, self.salary]
    