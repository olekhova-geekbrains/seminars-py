# 5. Реализуйте алгоритм перемешивания элементов списка. Без функции shuffle из модуля random, другие методы использовать можно.

import random


my_list = [3, 5, 29, 86, 2, 'ttt']


def mix(old_list):
    new_list = list(old_list)
    length = len(new_list)
    for i in range(length):
        rnd = random.randrange(length)
        tmp = new_list[i]
        new_list[i] = new_list[rnd]
        new_list[rnd] = tmp
    return new_list

print(my_list)
print(mix(my_list))