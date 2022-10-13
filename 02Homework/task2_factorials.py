# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда[1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)

import math


def fact(num):
    pr = []
    for i in range(1,num+1):
        pr.append(math.factorial(i))
    return pr


n = int(input('Введите натуральное число: '))
print(fact(n))
