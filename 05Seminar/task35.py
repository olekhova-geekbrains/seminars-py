# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Для работы с файлами используйте менеджер контекста.

def read_data(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as data:
        a = data.read().split()
        a = list(map(int, a))  # или a = [int(elem) for elem in a]
    return a


def check_data(my_list: list) -> int:
    for i in range(1, len(my_list)):
        if my_list[i] - 1 != my_list[i-1]:
            return my_list[i] - 1


a = read_data("file_35.txt")
print(check_data(a))
