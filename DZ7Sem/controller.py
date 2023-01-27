import csv
import json

from models import Person, J_Person


def read_base(text='base.csv'):
    if 'csv' in text:
        with open(text, 'r', encoding='utf-8') as data:
            base_reader = csv.reader(data, delimiter=',')
            base_employee = []
            for item in base_reader:
                base_employee.append(Person(int(item[0]), item[1], item[2]))
            return base_employee
    elif 'json' in text:
        with open(text, 'r', encoding='utf-8') as data:
            json_reader = json.load(data)['Person']
            base_person = []
            for item in json_reader:
                base_person.append(J_Person(item))
            return base_person
    
def add_person(person:Person, text='base.csv'):
    if find_person(person.name) == False:
        with open(text, 'a', newline='', encoding='utf-8') as data:
            base_writer = csv.writer(data, delimiter=',')
            base_writer.writerow(person.to_list_person())
            
            
def update_person(name, new_person, text='base.csv'):
    if find_person(name) != False:
        delete_person(name, text)
        add_person(new_person, text)


def delete_person(name, text='base.csv'):
    save_base_csv([x.to_list_person() for x in read_base() if name.lower() not in x.name.lower()], text)
    
    
def save_base_csv(to_list_person, text='output/base.csv'):
    text = 'output/base.csv' if text == "" else text
    with open(text, 'w', newline='', encoding='utf-8') as data:
        base_writer = csv.writer(data, delimiter=',')
        base_writer.writerows(to_list_person)
        

def save_base_json(persons, text='output/base.json'):
    text = 'output/base.json' if text == "" else text
    with open(text, 'w', encoding='utf-8') as f:
        json.dump({Person.__name__: persons}, f)
    print(f'Файл сохранён по адреcу "{text}"')


def find_id(text):
    result = max([x.id for x in read_base() if text.lower() in x.name.lower()])
    return result if result != [] else False
    
def find_person(text):
    result = [x for x in read_base() if text.lower() in x.name.lower()]
    return result if result != [] else False

def find_phone_number(text):
    result = [x for x in read_base() if text.lower() in x.phone_number.lower()]
    return result if result != [] else False
    
def next_id():
    max([x.id for x in read_base()])
    return max([x.id for x in read_base()])+1
