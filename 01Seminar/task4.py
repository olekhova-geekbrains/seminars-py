# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры: *
# - 6, 78 -> 7
# - 5 -> нет
# - 0, 34 -> 3

# num = float(input('Введите дробное число: '))


# d1 = int((num*10) % 10)
# print(d1)


num = input('Введите дробное число: ')
lst = num.split(".")
print(lst[1][0])


ch = num.find('.')
print(num[ch+1])


print(num[num.find(".")+1])
