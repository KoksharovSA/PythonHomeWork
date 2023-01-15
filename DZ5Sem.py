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

#task2()

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
    def is_win():
        return 0
    while True:
        while True:
            gamer_cell = input('Введите координату ячейки: ')
            if len(gamer_cell) == 2 \
                    and int(gamer_cell[0]) <= 3 \
                    and int(gamer_cell[1]) <= 3 \
                    and cells[int(gamer_cell[0])-1][int(gamer_cell[1])-1] == ' ':
                cells[int(gamer_cell[0])-1][int(gamer_cell[1])-1] = 'X'
                while True:
                    x = random.randint(0,2)
                    y = random.randint(0,2)
                    if cells[x][y] == ' ':
                        cells[x][y] = 'O'
                        break
                break
            else:
                print('Не верная координата ячейки или ячейка занята.')
        print(field())
        
    

task3()
# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
