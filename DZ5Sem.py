# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def task1(text):
    return ' '.join([x for x in text.split() if not 'абв' in x])


print(task1('Привет абваваорлпов чстмоыолабв абв мир'))


# 2.Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
def task2():
    candy = 121
    while True:
        if 28 < candy < 56:
            print(f'Всего конфет: {candy}')
            print("Программа победила!")
            break
        if candy < 29:
            print(f'Всего конфет: {candy}')
            print("Вы победили!")
            break
        print(f'Всего конфет: {candy}')
        while True:
            gamer_number = int(input('Сколко конфет возьмёте(от 1 до 28)?: '))
            if 0 < gamer_number < 29:
                break
            else:
                print('Неверное количество попробуйте ещё раз.')
        candy = candy - gamer_number
        program_number = {candy % 28 != 0 and candy % 28 != 1: (candy % 28) - 1,
                          candy % 28 != 0 and candy % 28 == 1: 1,
                          candy % 28 == 0 and candy != 56: 27,
                          candy == 56: 27}[True]
        print(f'Прграмма взяла: {program_number}')
        candy = candy - program_number


# task2()

# 3.Создайте программу для игры в ""Крестики-нолики"".
import random


def task3():
    cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    def field():
        return f'   1   2   3\n' \
               f' -------------\n' \
               f'1| {cells[0][0]} | {cells[0][1]} | {cells[0][2]} |\n' \
               f' -------------\n' \
               f'2| {cells[1][0]} | {cells[1][1]} | {cells[1][2]} |\n' \
               f' -------------\n' \
               f'3| {cells[2][0]} | {cells[2][1]} | {cells[2][2]} |\n' \
               f' -------------'
    
    print(field())
    
    def who_win():
        winner = cells[0][0] + cells[0][1] + cells[0][2] + '-' + \
                 cells[1][0] + cells[1][1] + cells[1][2] + '-' + \
                 cells[2][0] + cells[2][1] + cells[2][2] + '-' + \
                 cells[0][0] + cells[1][0] + cells[2][0] + '-' + \
                 cells[0][1] + cells[1][1] + cells[2][1] + '-' + \
                 cells[0][2] + cells[1][2] + cells[2][2] + '-' + \
                 cells[0][0] + cells[1][1] + cells[2][2] + '-' + \
                 cells[0][2] + cells[1][1] + cells[2][0]
        result = {'XXX' in winner.split('-'): [False, 'Победил X'],
                  'OOO' in winner.split('-'): [False, 'Победил O'],
                  'XXX' not in winner.split('-') and 'OOO' not in winner.split('-'): [True, '', winner],
                  ' ' not in winner: [False, 'Игра окончена']}[True]
        return result
    
    def correct_coordinate(coordinate):
        if len(gamer_cell) == 2 \
                and int(gamer_cell[0]) <= 3 \
                and int(gamer_cell[1]) <= 3 \
                and cells[int(gamer_cell[0]) - 1][int(gamer_cell[1]) - 1] == ' ':
            return True
        else:
            return False
    
    def ai():
        dict_response = {cells[0][0] == 'X' and cells[0][1] == 'X': '02',
                         cells[0][1] == 'X' and cells[0][2] == 'X': '00',
                         cells[0][0] == 'X' and cells[0][2] == 'X': '01',
                         cells[1][0] == 'X' and cells[1][1] == 'X': '12',
                         cells[1][1] == 'X' and cells[1][2] == 'X': '10',
                         cells[1][0] == 'X' and cells[1][2] == 'X': '11',
                         cells[2][0] == 'X' and cells[2][1] == 'X': '22',
                         cells[2][1] == 'X' and cells[2][2] == 'X': '20',
                         cells[2][0] == 'X' and cells[2][2] == 'X': '21',
                         cells[0][0] == 'X' and cells[1][0] == 'X': '20',
                         cells[1][0] == 'X' and cells[2][0] == 'X': '00',
                         cells[0][0] == 'X' and cells[2][0] == 'X': '10',
                         cells[0][1] == 'X' and cells[1][1] == 'X': '21',
                         cells[1][1] == 'X' and cells[2][1] == 'X': '10',
                         cells[0][1] == 'X' and cells[2][1] == 'X': '11',
                         cells[0][2] == 'X' and cells[1][2] == 'X': '22',
                         cells[1][2] == 'X' and cells[2][2] == 'X': '02',
                         cells[0][2] == 'X' and cells[2][2] == 'X': '12',
                         cells[0][0] == 'X' and cells[1][1] == 'X': '22',
                         cells[2][2] == 'X' and cells[1][1] == 'X': '00',
                         cells[0][0] == 'X' and cells[2][2] == 'X': '11',
                         cells[0][2] == 'X' and cells[1][1] == 'X': '20',
                         cells[2][0] == 'X' and cells[1][1] == 'X': '02',
                         cells[2][0] == 'X' and cells[0][2] == 'X': '11'}
        result = [y for x, y in dict_response.items() if x == True]
        return result[random.randint(0, len(result)-1)]
    
    while who_win()[0]:
        while who_win()[0]:
            gamer_cell = input('Введите координату ячейки: ')
            if correct_coordinate(gamer_cell):
                cells[int(gamer_cell[0]) - 1][int(gamer_cell[1]) - 1] = 'X'
                while who_win()[0]:
                    if 'XX' in who_win()[2]:
                        x = int(ai()[0])
                        y = int(ai()[1])
                    else:
                        x = random.randint(0, 2)
                        y = random.randint(0, 2)
                    if cells[x][y] == ' ':
                        cells[x][y] = 'O'
                        break
                break
            else:
                print('Не верная координата ячейки или ячейка занята.')
        print(field())
        print(who_win()[1])


task3()


# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
def task4(dir_input, dir_output):
    with open(dir_input, 'r') as data_in:
        list_input = data_in.readlines()
        with open(dir_output, 'w') as data_out:
            for string in [x.replace('\n', '') for x in list_input]:
                result = ''
                count = 0
                for index, element in enumerate(string):
                    if index == 0:
                        count += 1
                    else:
                        if string[index] == string[index - 1] and index != len(string) - 1:
                            count += 1
                        elif index == len(string) - 1:
                            if string[index] == string[index - 1]:
                                result += f'{count + 1}{string[index]} '
                            else:
                                result += f'{count}{string[index - 1]} '
                                count = 1
                                result += f'{count}{string[index]} '
                        else:
                            result += f'{count}{string[index - 1]} '
                            count = 1
                data_out.write(f'{result}\n')


task4('file5SemInput.txt', 'file5SemOutput.txt')
