# ввод числа
def data_in() -> str:
    return input('Введите рациональное число через / ')

# ввод оператора
def data_op() -> str:
    return input('Введите оператор ')


# вывод в консоль
def show_data(data: list):
    numer, denom = data
    if numer % denom == 0:
        return print(f'Результат вычисления: {int(numer / denom)}')
    else:
        return print(f'Результат вычисления: {numer}/{denom}')