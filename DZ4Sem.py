# 1.Вычислить число π c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

def task1(number: float):
    print(round(math.pi, len(str(number).split('.')[1])))

task1(0.001)
task1(0.1)
task1(0.0001)

# 2.Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.
def task2(n):
    ans = [1,]
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    print(ans)

task2(5)
task2(50)
task2(100)

# 3.Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
def task3(n):
    print([int(x) for x in n.split() if n.count(x) == 1])

task3('10 22 55 44 88 44 66')


# 4.Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

def task4(n):
    with open('file_task4_4sem.txt', 'a') as data:
        polynomial_of_degree_n = ''
        while n!=0:
            if n < 2 :
                result1 = f'{random.randint(0, 100)}*x + '
                result2 = f'{random.randint(0, 100)} = 0\n'
                if result1 == '0*x + ':
                    result1 = ''
                if result2 == '0 = 0':
                    result2 = '= 0'
                polynomial_of_degree_n += result1 + result2
                break
            else:
                polynomial_of_degree_n += f'{random.randint(0, 100)}*x^{n} + '
                n -= 1
        data.writelines(polynomial_of_degree_n)
        
task4(4)
task4(6)
task4(2)
task4(1)

# 5.Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.
def task5(file1, file2):
    with open(file1, 'r') as data:
        polynomial1 = data.read()
    with open(file2, 'r') as data:
        polynomial2 = data.read()
    result1 = {x: (int(x.split('^')[1]) if '^' in x else 0) for x in
               polynomial1.replace(' ', '').split('+')}
    result2 = {x: (int(x.split('^')[1]) if '^' in x else 0) for x in
               polynomial2.replace(' ', '').split('+')}
    result = ''
    long_polynomial = result1 if len(polynomial1) >= len(polynomial2) else result2
    short_polynomial = result1 if len(polynomial1) < len(polynomial2) else result2
    for key, value in long_polynomial.items():
        if value in short_polynomial.values() and '=' not in key :
            k = int(key.split('*')[0]) + int([x for x, y in short_polynomial.items() if value == y][0].split('*')[0])
            result += f"{k}*{key.split('*')[1]}+"
        elif '=' in key:
            k = int(key.split('=')[0]) + int([x for x, y in short_polynomial.items() if '=' in x][0].split(
                '=')[0])
            result += f'{k}=0'
        else:
            result += f'{key}+'
    with open('file3.txt', 'a') as data:
        data.writelines(result)
    
task5('file1.txt', 'file2.txt')
