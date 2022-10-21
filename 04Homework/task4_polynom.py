# 4. Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов многочлена и записать в файл многочлен степени k.
# Коэффициенты должны быть случайными числами в диапазоне от 1 до 100
# Пример:
# - k = 2 = > 6*x ^ 2 + 4*x + 5 = 0 или x ^ 2 + 5 = 0 или 10*x ^ 2 = 0
# Усложнение: Коэффициенты в полиноме могут быть нулевыми.
# Примечание Создать три функции:
# 1) Функция формирования полинома. аргумент: степень полинома; возвращает полином. Коэффициенты вычисляются случайными.
#     Полином удобно представить как словарь или как список коэффициентов. (на ваш выбор)
#     В словаре степени будут ключами, в списке - индексами.
#     Например k=3= > 6*x ^ 3 + 4*x + 5. Словарь будет такой: {3: 6, 2: 0, 1: 4, 0: 5}. А список такой [5, 4, 0, 6]
#     2) Функция формирование строки-полинома. Аргумент: полином(в вид словаря или списка).
#     Возвращает строку вида '6*x^3 + 4*x + 5'
#     Примечание: Обратите внимание на запись первой и нулевой степени, а также учет нулевого коэффициента.
#     Для формирования строки удобно использовать join
#     3) Функция записи строки-полинома в файл. Аргументы: имя файла и строка-полином.

from random import randint


def generate_polynom(n: int, min_coeff: int, max_coeff: int) -> list:
    coeffs = [randint(min_coeff, max_coeff) for _ in range(n + 1)]
    return coeffs


def generate_polynom_dict(n: int, min_coeff: int, max_coeff: int) -> dict:
    coeffs = {a: randint(min_coeff, max_coeff) for a in range(n + 1)}
    return coeffs


def stringify_polynom(coeffs: list) -> str:
    terms = []
    for i, coeff in reversed(list(enumerate(coeffs))):
        if coeff == 0:
            continue
        if i == 0:
            terms.append(f'{coeff}')
        elif i == 1:
            terms.append('x' if coeff == 1 else f'{coeff}*x')
        else:
            terms.append(f'x^{i}' if coeff == 1 else f'{coeff}*x^{i}')
    return ' + '.join(terms)


def stringify_polynom_dict(coeffs: dict) -> str:
    terms = []
    pows = list(coeffs.keys())
    pows.sort(reverse=True)
    for el in pows:
        if coeffs[el] == 0:
            continue
        if el == 0:
            terms.append(f'{coeffs[el]}')
        elif el == 1:
            terms.append('x' if coeffs[el] == 1 else f'{coeffs[el]}*x')
        else:
            terms.append(f'x^{el}' if coeffs[el] == 1 else f'{coeffs[el]}*x^{el}')
    return ' + '.join(terms)


def write_to_file_polynom(file_name: str, polynom: str):
    with open(file_name, mode = 'w') as file:
        file.write(polynom)


if __name__ == "__main__":


    MIN_COEFF = 0
    MAX_COEFF = 5
    POW = 10


    pol = generate_polynom(POW, MIN_COEFF, MAX_COEFF)
    pol_s = stringify_polynom(pol)
    write_to_file_polynom('polynom.txt', pol_s)


    pol1 = generate_polynom_dict(POW, MIN_COEFF, MAX_COEFF)
    pol1_s = stringify_polynom_dict(pol1)
    write_to_file_polynom('polynom1.txt', pol1_s)
