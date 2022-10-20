# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0
# Для обоих вариантов:
# - действительные корни
# - комплексные корни
# Примечание:
#  - проверить нужное условие перед вычислением корней
# - найти нужные пакеты стандартной библиотеки и функции в них для вычисления кв. корня.

# from math import sqrt as sq1
# from cmath import sqrt as sq2


# n_a = 3
# n_b = 6
# n_c = 3
# D = n_b ** 2 - 4 * n_a * n_c
# if D > 0:
#     x1 = (-n_b + sq1(D)) / 2 * n_a
#     x2 = (-n_b - sq1(D)) / 2 * n_a
# elif D == 0:
#     x1 = -n_b / 2 * n_a
#     x2 = None
# else:
#     x1 = (-n_b + sq2(D)) / 2 * n_a
#     x2 = (-n_b - sq2(D)) / 2 * n_a
# print(x1, x2)

from math import sqrt as sq
from cmath import sqrt as csq

a = 99
b = 3
c = 4

dis = b**2 - 4 * a * c
# Присваивание в лоб
# if dis > 0:
# sqrt = sq
# else:
# sqrt = csq

# Тернарный оператор
sqrt = sq if dis > 0 else csq


x1 = (-b + sqrt(dis))/(2*a)
x2 = (-b - sqrt(dis))/(2*a)


print(f"Корни уравнения: {x1:.2f} и {x2:.2f}")