# Пример:
# - для k = 8 список будет выглядеть так: [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# Примечание:

#     Алгоритм смотрим тут: https: // ru.wikipedia.org/wiki/Негафибоначчи
#     Вам понадобится рекурсивный вызов функции или сделайте в виде списка.

def fibonacci(n):
    fib = [0]
    if n == 0:
        return fib
    fib.append(1)
    fib.insert(0, 1)
    if n == 1:
        return fib
    for i in range(2, n + 1):
        item = fib[- 2] + fib[- 1]
        fib.append(item)
        fib.insert(0,(-1)**(i + 1)*item)
    return fib


def fibonacci1(n):
    fib = [0]*(2*n + 1)
    if n == 0:
        return fib
    fib[n] = 0
    fib[n+1] = 1
    fib[n-1] = 1
    for i in range(n - 1):
        fib[n + i + 2] = fib[n + i + 1] + fib[n + i]
        fib[n - i - 2] = (-1)**(i + 1)*fib[n + i + 2]
    return fib


while True:
    data = input('Введите натуральное число: ')
    if data == "": break
    if not data.isdigit():
        print('Неправильный ввод. Введите натуральное число: ')
    else: 
        num = int(data)
        break

print(fibonacci(num))
print(fibonacci1(num))
