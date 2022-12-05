# 36. Дан список целых чисел. Например[1, 5, 2, 3, 4, 6, 1, 7]
# Пользователь выбирает целое число - элемент списка.
# Создайте список, в который попадают числа, описываемые любую возрастающую последовательность, 
# начиная с выбранного пользователем элемента
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] = > выбрано 1 = > [1, 5, 6, 7]
# [1, 5, 2, 3, 4, 6, 1, 7] = > выбрано 3 = > [3, 4, 6, 7]
# Усложнение: Вывести список ВСЕХ возможных возрастающих последовательностей
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 5]
# выбрано 3 = > [3, 4, 5], [3, 4, 6], [3, 5], [3, 6]
# выбрано 1 = > [1, 2, 3, 4, 5], [1, 2, 3, 4, 6], [1, 2, 3, 5], [1, 2, 3, 6], [1, 2, 4, 5],
# [1, 2, 4, 6], [1, 2, 5], [1, 2, 6], [1, 3, 4, 5], [1, 3, 4, 6] и т.п.


# def get_ascending_sequence(lst: list, number: int) -> list:
#     seq = [number]
#     start_index = lst.index(number) + 1
#     finish_index = len(lst)
#     current_number = number
#     for idx in range(start_index, finish_index):
#         if current_number < lst[idx]:
#             seq.append(lst[idx])
#             current_number = lst[idx]
#     return seq


def get_ascending_sequence(lst: list, number: int) -> list:
    seq = [number]
    start_index = lst.index(number) + 1
    finish_index = len(lst)
    current_number = number
    for idx in range(start_index, finish_index):
        if current_number < lst[idx]:
            seq.append(lst[idx])
            current_number = lst[idx]
    return seq

my_list = [1, 5, 2, 3, 4, 6, 1, 7]


while True:
    data = input(f'Выберете элемент из списка {my_list}: ')
    if data == '': break
    if data in str(my_list): 
        num = int(data)
        break

print(get_ascending_sequence(my_list, num))
