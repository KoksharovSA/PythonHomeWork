import controller as cr
from models import Employee

def show_menu():
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def event_loop():
    while True:
        number = show_menu()
        if number == 1:
            employees = cr.find_employee(input('Введите фамилию сотрудника: '))
            for item in employees:
                print(str(item))
        elif number == 2:
            rank = cr.find_rank(input('Введите должность: '))
            for item in rank:
                print(str(item))
        elif number == 3:
            salary = cr.find_salary(int(input('Введите оклад: ')))
            for item in salary:
                print(str(item))
        elif number == 4:
            cr.add_employee(Employee(cr.next_id(),input('Введите ФИО: '), input('Введите должность: '), int(input('Введите '
                                                                                                       'оклад: '))))
        elif number == 5:
            cr.delete_employee(input('Введите фамилию сотрудника: '))
        elif number == 6:
            cr.update_employee(input('Введите фамилию сотрудника: '),
                               Employee(cr.next_id(),input('Введите ФИО: '), input('Введите должность: '),
                                        int(input('Введите оклад: '))))
        elif number == 7:
            cr.save_base_json([x.to_dict() for x in cr.read_base()], input('Введите имя сохраняемого файла:'))
        elif number == 8:
            cr.save_base_csv([x.to_list_employee() for x in cr.read_base()], input('Введите имя сохраняемого файла:'))
        elif number == 9:
            break
        else:
            print('Неверный номер действия.')
