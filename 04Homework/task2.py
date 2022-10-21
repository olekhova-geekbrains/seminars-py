# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Написать функцию, которая принимает аргумент - целое число и возвращает список его простых множителей.
# Пример:
# simple_number(147420) = > [2, 3, 5, 7, 13]
# simple_number(374220) = > [2, 3, 5, 7, 11]

def prime(num: int) -> list:
    pr = []
    new_num = num
    # пока делится на 2, делим на 2
    # и пока делится на 3, делим на 3
    for i in range(2, 4):
        while new_num % i == 0:
            pr.append(i)
            new_num //= i
    k = 1
    while (6*k - 1)*(6*k - 1) <= num:
        i = 6*k - 1
        while new_num % i == 0:
            pr.append(i)
            new_num //= i
        i = 6*k + 1
        while new_num % i == 0:
            pr.append(i)
            new_num //= i
        k += 1
    if new_num != 1:
        pr.append(new_num)
    return list(set(pr))


n = int(input('Введите число: '))
print(prime(n))
