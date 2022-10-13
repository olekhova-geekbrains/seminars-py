# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n=4 [2, 2.25, 2.37, 2.44]
# Сумма 9.06


def sequence(num: int) -> list:
    seq = []
    for i in range(1, num + 1):
        item = (1 + 1 / i)**i
        seq.append(round(item, 2))
    return seq


def sum_seq(sq: list) ->float:
    sum_seq = sum(sq)
    return sum_seq


n = int(input('Введите натуральное число: '))
sq = sequence(n)
print(sq)
print(sum_seq(sq))
