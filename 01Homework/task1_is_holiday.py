# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример: *
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def is_holiday(num):
    if num == 6 or num == 7:
        return ('да')
    elif 1 <= num <= 5:
        return ('нет')
    else:
        return ('некорректное число')


n = int(input('Введите число - номер дня недели: '))
print(is_holiday(n))
