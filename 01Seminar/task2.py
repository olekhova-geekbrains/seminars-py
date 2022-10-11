# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90


my_list = []
for i in range(5):
    my_list.append(int(input('Введите число: ')))
print(my_list)


max_el = my_list[0]


for el in my_list:
    if el > max_el: max_el = el
print(max)

print(f"Максимальное число из {my_list} будет {max(my_list)}")
