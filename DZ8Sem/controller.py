import csv
import json

from models import Employee, J_Employee


def read_base(text='base.csv'):
    if 'csv' in text:
        with open(text, 'r', encoding='utf-8') as data:
            base_reader = csv.reader(data, delimiter=',')
            base_employee = []
            for item in base_reader:
                base_employee.append(Employee(int(item[0]), item[1], item[2], int(item[3])))
            return base_employee
    elif 'json' in text:
        with open(text, 'r', encoding='utf-8') as data:
            json_reader = json.load(data)['Employee']
            base_employee = []
            for item in json_reader:
                base_employee.append(J_Employee(item))
            return base_employee
    
def add_employee(employee:Employee, text='base.csv'):
    if find_employee(employee.name) == False:
        with open(text, 'a', newline='', encoding='utf-8') as data:
            base_writer = csv.writer(data, delimiter=',')
            base_writer.writerow(employee.to_list_employee())
            
            
def update_employee(name, new_employee, text='base.csv'):
    if find_employee(name) != False:
        delete_employee(name, text)
        add_employee(new_employee, text)


def delete_employee(name, text='base.csv'):
    save_base_csv([x.to_list_employee() for x in read_base() if name.lower() not in x.name.lower()], text)
    
    
def save_base_csv(to_list_employees, text='output/base.csv'):
    text = 'output/base.csv' if text == "" else text
    with open(text, 'w', newline='', encoding='utf-8') as data:
        base_writer = csv.writer(data, delimiter=',')
        base_writer.writerows(to_list_employees)
        

def save_base_json(employees, text='output/base.json'):
    text = 'output/base.json' if text == "" else text
    with open(text, 'w', encoding='utf-8') as f:
        json.dump({Employee.__name__: employees}, f)
    print(f'Файл сохранён по адреcу "{text}"')


def find_id(text):
    result = max([x.id for x in read_base() if text.lower() in x.name.lower()])
    return result if result != [] else False
    
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
