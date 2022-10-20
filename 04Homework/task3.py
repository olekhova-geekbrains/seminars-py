# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


def unique(lst: list) -> list:
    res = []
    for s in lst:
        if lst.count(s) == 1:
            res.append(s)
    return res


my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(unique(my_list))
