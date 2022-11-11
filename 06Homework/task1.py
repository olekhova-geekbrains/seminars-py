# 1. Сформировать список нечетных целых чисел от 0 до N, квадрат которых 
# меньше 200. Использовать comprehensions


def odd_list(num: int) -> list:
    return [i for i in range(1, num + 1, 2) if i*i < 200 ]


number = int(input('Введите натуральное число: '))
print(odd_list(number))