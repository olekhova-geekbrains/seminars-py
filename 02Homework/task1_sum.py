# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0, 56 -> 11
# - 187, 6778 -> 44
# Примечание: Программа должна работать для любого количества цифр в числе.


def sum1(num: str) ->int:
  sum = 0
  for i in num:
      if i.isdigit():
          sum += int(i)
  return sum


def sum2(num: str):
    new_num = int(num.replace('.', ''))
    sum = 0
    while new_num >= 10:
        sum += new_num % 10
        new_num //=  10
    return sum + new_num


n = input('Введите вещественное число: ')
print(sum1(n))
print(sum2(n))