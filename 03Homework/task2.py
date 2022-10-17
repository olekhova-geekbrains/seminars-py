# 2. Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math


def prod_pair(lst):
    length = len(lst)
    prods = []
    for i in range(math.ceil(length / 2)):
        prod = lst[i] * lst[length - 1 - i]
        prods.append(prod)
    return prods


my_list = [2, 3, 4, 5, 6]
print(prod_pair(my_list))


my_list1 = [2, 3, 5, 6]
print(prod_pair(my_list1))