# 27. Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# Пример: Строка " 12 34 78 9894 4373 123"
# Усложнение: создайте строку чисел через случайные числа. Подсказка: используйте метод строки join для создания строки.


my_list = " 12 34 78 9894 4373 123"
my_list1 = my_list.split()
print(my_list)
print(my_list1)
print(max(my_list1), min(my_list1))


from random import randint
my_list3 = ' '.join([str(randint(10, 100)) for i in range(randint(5, 10))])
my_list4 = my_list3.split()
print(my_list3)
print(my_list4)
print(max(my_list4), min(my_list4))
