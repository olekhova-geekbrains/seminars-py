# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81


# n = int(input('введите число N: '))
# for i in range(n):
#     print((-3)**i, end=' ')


n = int(input(f'Введите число N '))
n_list = []
x = 1
for i in range(n):
    n_list.append(x)
    x *= -3
print(n_list)
