import random


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
    if len(coordinate) == 2 \
            and int(coordinate[0]) <= 3 \
            and int(coordinate[1]) <= 3 \
            and cells[int(coordinate[0]) - 1][int(coordinate[1]) - 1] == ' ':
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
    return result[random.randint(0, len(result) - 1)]


def ttt(coordinate):

    if who_win()[0]:
        if who_win()[0]:
            gamer_cell = coordinate
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
                return who_win()[1]
            else:
                return('Не верная координата ячейки или ячейка занята.')
        else:
            print(who_win()[1])
            return f'{field()}\n{who_win()[1]}'