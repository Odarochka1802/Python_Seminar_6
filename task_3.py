# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)*
# многочлена и записать в файл многочлен степени k.
#     *Пример:*
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0

from random import randint
from sympy import symbols
from math import prod

print('Введите натуральную степень k:')
k = int(input())


def write_file(st):
    with open('task_04.txt', 'a', encoding="utf-8") as file:
        file.write(st)


def create_list(k):
    lst = []
    max_val = 100
    lst = [randint(-max_val, max_val) for i in range(k)]+[randint(1, max_val)]
    return lst


def create_str(sp):
    x = symbols('x')
    return f"{sum(map(prod,zip(sp,[x**i for i in range(k+1)])))} = 0"


koef = create_list(k)
write_file(f"Введите натуральную степень k:{k}\n {create_str(koef)}\n")
