# 1. Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:    
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd_index(lst):
    if len(lst) < 2:
        return 'Нет нечетных индексов'
    sum = 0
    for i in range(1, len(lst), 2):
        sum += lst[i]
    return sum


my_list = [2, 3, 5, 9, 3]
print(sum_odd_index(my_list))


print(sum(my_list[1::2]))
