# 4. Задайте список из элементов, заполненных числами из промежутка[-N, N]. Задайте два числа - позиции(индексы) в исходном списке это границы диапазона. Найдите произведение элементов списка в указанном диапазоне индексов
# Пример:
# N = 6
# Пример списка чисел: [-2, -5, 4, 1, 4, 1, 2, -5, -3, 0, -6, -6, 5]
# границы диапазона: 2, 5
# Произведение для[4, 1, 4, 1] равно 16

import random
import math


def generate_list(length: int, n: int) -> list:
    l = []
    for i in range(length):
        item = random.randint(-n, n)
        l.append(item)
    return l



def prod(l:list, start: int, finish: int):
    new_list = l[start:finish + 1]
    print(new_list)
    return math.prod(new_list)


length = int(input('Введите длину последовательности: '))
n = int(input('Введите n, в котором должны быть элементы последовательности [-n,n]: '))


start = int(input('Введите стартовый индекс элемента для умножения: '))
while start > length - 1:
    print('Неправильно, введите еще раз')
    start = int(input('Введите стартовый индекс элемента для умножения: '))


finish = int(input('Введите конечный индекс элемента для умножения: '))
while finish > length - 1 or finish < start:
    print('Неправильно, введите еще раз')
    finish = int(input('Введите стартовый индекс элемента для умножения: '))


my_list = generate_list(length, n)
print(my_list)
print(prod(my_list, start, finish))
