# 13. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.


str_scope="123hgfd123jgdg1234ritrpr1"
str_find="12"
# [MAIN] Основной вариант решения:
# [Вопрос группе] Работа со строками: изобретаем или ищем клады

# 1. Ищем клады
print(f"Кол-во вхождений: {str_scope.count(str_find)}")

# 2. Изобретаем велосипеды
# [*] - Усложнение: Подумать об эффективности
# Что у нас внутри цикла
find_count=0
for i in range(len(str_scope)):
    str_block=str_scope[i:i + len(str_find)]
    if str_block == str_find:
        find_count += 1
print(f"Кол-во вхождений: {find_count}")



# str_scope='1285564dasd152asdasd12asdasdaswqe1234'
# str_find='12'

# find_count=0
# for i in range(len(str_scope)):
#     if str_find == str_scope[i:i+len(str_find)]:
#         find_count += 1

# print(find_count)
