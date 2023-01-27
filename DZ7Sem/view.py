import controller as cr
from models import Person

def show_menu():
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Вывести всю базу номеров")
    print("2. Найти номер телефона по фамилии человека")
    print("3. Найти контакт по номеру телефона")
    print("4. Добавить новый контакт")
    print("5. Удалить контакт")
    print("6. Обновить данные контакта")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def event_loop():
    while True:
        number = show_menu()
        if number == 1:
            for item in cr.read_base():
                print(f'{str(item)}\n')
        elif number == 2:
            name = cr.find_person(input('Введите фамилию человека: '))
            if not name:
                print('В базе нет такого контакта')
            else:
                for item in name:
                    print(str(item))
        elif number == 3:
            phone_number = cr.find_phone_number(input('Введите номер телефона: '))
            if not phone_number:
                print('В базе нет такого контакта')
            else:
                for item in phone_number:
                    print(str(item))
        elif number == 4:
            cr.add_person(Person(cr.next_id(),input('Введите ФИО: '), input('Введите номер телефона: ')))
        elif number == 5:
            cr.delete_person(input('Введите фамилию контакта: '))
        elif number == 6:
            cr.update_person(input('Введите фамилию контакта: '),
                               Person(cr.next_id(),input('Введите ФИО: '), input('Введите номер телефона: ')))
        elif number == 7:
            cr.save_base_json([x.to_dict() for x in cr.read_base()], input('Введите имя сохраняемого файла:'))
        elif number == 8:
            cr.save_base_csv([x.to_list_person() for x in cr.read_base()], input('Введите имя сохраняемого файла:'))
        elif number == 9:
            break
        else:
            print('Неверный номер действия.')
