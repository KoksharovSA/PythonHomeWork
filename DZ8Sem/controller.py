import csv

from models import Employee


def read_base(text='base.csv'):
    with open(text, 'r', encoding='utf-8') as data:
        base_reader = csv.reader(data, delimiter=',')
        base_employee = []
        for item in base_reader:
            base_employee.append(Employee(int(item[0]), item[1], item[2], int(item[3])))
        return base_employee
    
def add_employee(employee:Employee, text='base.csv'):
    if find_employee(employee.name) == False:
        with open(text, 'a', newline='', encoding='utf-8') as data:
            base_writer = csv.writer(data, delimiter=',')
            base_writer.writerow(employee.list_employee())
            
            
def update_employee(name, new_employee, text='base.csv'):
    if find_employee(name) != False:
        list_employees = [x for x in read_base() if x.name not in name].append(new_employee)
        save_base_csv(list_employees, text)


def delete_employee(name, new_employee, text='base.csv'):
    return 0
    
    
def save_base_csv(list_employees, text='base.csv'):
    with open(text, 'w', newline='', encoding='utf-8') as data:
        base_writer = csv.writer(data, delimiter=',')
        for item in list_employees:
            base_writer.writerow(item.list_employee())
 
    
def find_employee(text):
    result = [x for x in read_base() if text.lower() in x.name.lower()]
    return result if result != [] else False

def find_rank(text):
    result = [x for x in read_base() if text.lower() in x.rank.lower()]
    return result if result != [] else False
    
def find_salary(number: int, sign: str ='='):
    if sign == '<':
        return [x for x in read_base() if number <= x.salary]
    if sign == '>':
        return [x for x in read_base() if number >= x.salary]
    if sign == '=':
        return [x for x in read_base() if number == x.salary]
    else:
        return False
    
def next_id():
    max([x.id for x in read_base()])
    return max([x.id for x in read_base()])+1

# result = [str(x) for x in read_base() if x.id == 1]
# print(result)
print(find_employee('иван'))
print(find_employee('asd'))
print(find_rank('главный'))
print(find_salary(50000, '>'))
print(find_salary(50000, '<'))
print(find_salary(50000))
add_employee(Employee(next_id(), 'Крузенштерн И.Ф.', 'Капитан', 60000))
update_employee('крузенш', Employee(find_employee('Крузенштерн И.Ф.')[0].id, 'Крузенштерн И.Ф.', 'Капитан', 160000))

