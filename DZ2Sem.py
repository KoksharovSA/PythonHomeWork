# Урок 2. Знакомство с Python. Продолжение
#
# (Последняя задача семенара)
# Для натурального n создать словарь индекс-значение, состоящий из элементов
# последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def task_semenar(number):
    print(
        f'Для n = {number}: {dict(zip(range(1, number + 1), [3 * x + 1 for x in range(1, number + 1)]))}')

print('----------\nНе решённая задача из 2-го семенара')
task_semenar(6)

# 1.Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
def task1(number):
    print(f'{number} -> {sum([int(x) for x in str(number) if x.isdigit()])}')

print('----------\nЗадача №1 Сумма цифр числа')
task1(6782)
task1(0.56)

# 2.Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
from math import factorial


def task2(N):
    print(f'Пусть N = {N}, тогда {[factorial(x) for x in range(1, N + 1)]}')

print('----------\nЗадача №2 Список факториалов')
task2(4)


# 3.Задайте список из n чисел последовательности (1+1/n)**n  и выведите на
# экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def task3(n):
    list_elements = [round(((1 + 1 / x) ** x), 3) for x in range(1, n + 1)]
    print(f'Для n = {n}: {dict(zip(range(1, n + 1), list_elements))} \nСумма '
          f'элементов: {sum(list_elements)}')


print('----------\nЗадача №3 Список из n чисел последовательности (1+1/n)**n и их сумма')
task3(6)

# 4.Задайте список из N элементов, заполненных числами из промежутка [-N,
# N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
from math import prod


def task4(N, elements_multiplication):
    with open(elements_multiplication, 'r') as fe:
        list_elements = [int(element.replace('\n', ''))
                         for element in fe.readlines()]
    print(list(range(-N, N + 1)))
    print(prod([range(-N, N + 1)[x] for x in list_elements]))

print('----------\nЗадача №4 Список из N элементов [-N, N], и произведение '
      'элементов на позициях из файла')
task4(5, 'elements_multiplication.txt')

# 5.Реализуйте алгоритм перемешивания списка.
import random


def task5(present_list: list):
    return [present_list[x] for x in random.sample(range(0, len(present_list)),len(present_list))]

print('----------\nЗадача №5 Алгоритм перемешивания списка')
print(task5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(task5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(task5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
