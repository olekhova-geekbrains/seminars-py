# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние
# между ними в 2D пространстве.
# Пример:
# - A(3, 6)
# B(2, 1) -> 5, 09
# - A(7, -5)
# B(1, -1) -> 7, 21


import math

def dist(x1, y1, x2, y2):
    d = round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2),2)
    return d
    

# a_x = int(input('Введите координату x первой точки: '))
# a_y = int(input('Введите координату y первой точки: '))
# b_x = int(input('Введите координату x второй точки: '))
# b_y = int(input('Введите координату y второй точки: '))
point_list = []
for i in range(4):
    point_list.append(int(input('Введите координату: ')))


print(
    f'Расстояние между точками: {dist(point_list[0], point_list[1], point_list[2], point_list[3])}')

