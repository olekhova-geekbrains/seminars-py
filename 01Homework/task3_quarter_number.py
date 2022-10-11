# Напишите программу, которая принимает на
# вход координаты точки(X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# - x = 34
# y = -30 -> 4
# - x = 2
# y = 4 -> 1
# - x = -34
# y = -30 -> 3

def quarter_number(x, y):
    if x == 0 and y == 0:
        return 'начало координат'
    if x == 0:
        return 'ось y'
    if y == 0:
        return 'ось x'
    if x > 0 and y > 0:
        return '1 четверть'
    if x < 0 and y > 0:
        return '2 четверть'
    if x < 0 and y < 0:
        return '3 четверть'
    if x > 0 and y < 0:
        return '4 четверть'
    return 'это не должно случится'


a = int(input('Введите первую координату: '))
b = int(input('Введите вторую координату: '))
print(quarter_number(a, b))
