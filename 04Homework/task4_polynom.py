# 4. Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов многочлена и записать в файл многочлен степени k.
# Коэффициенты должны быть случайными числами в диапазоне от 1 до 100
# Пример:
# - k = 2 = > 6*x ^ 2 + 4*x + 5 = 0 или x ^ 2 + 5 = 0 или 10*x ^ 2 = 0
# Усложнение: Коэффициенты в полиноме могут быть нулевыми.
# Примечание Создать три функции:
# 1) Функция формирования полинома. аргумент: степень полинома; возвращает полином. Коэффициенты вычисляются случайными.
#     Полином удобно представить как словарь или как список коэффициентов. (на ваш выбор)
#     В словаре степени будут ключами, в списке - индексами.
#     Например k=3= > 6*x ^ 3 + 4*x + 5. Словарь будет такой: {3: 6, 2: 0, 1: 4, 0: 5}. А список такой [5, 4, 0, 6]
# 2) Функция формирование строки-полинома. Аргумент: полином(в вид словаря или списка).
#     Возвращает строку вида '6*x^3 + 4*x + 5'
#     Примечание: Обратите внимание на запись первой и нулевой степени, а также учет нулевого коэффициента.
#     Для формирования строки удобно использовать join
# 3) Функция записи строки-полинома в файл. Аргументы: имя файла и строка-полином.
import random


def generate_polynom(n: int, min_coeff: int, max_coeff: int) -> list:
    coeffs = [random.randint(min_coeff, max_coeff) for i in range(n + 1)]
    return coeffs


def generate_polynom_dict(n: int, min_coeff: int, max_coeff: int) -> dict:
    coeffs = {a: random.randint(min_coeff, max_coeff) for a in range(n + 1)}
    return coeffs


def stringify_polynom(coeffs: list) -> str:
    terms = []
    for i, coeff in reversed(list(enumerate(coeffs))):
        if coeff == 0:
            continue
        if i > 0:
            terms.append(f'{coeff}*x^{i}')
        else:
            terms.append(f'{coeff}')
    return ' + '.join(terms)


def stringify_polynom_dict(coeffs: dict) -> str:
    terms = []
    for key, value in coeffs.items():
        if value == 0:
            continue
        if key > 0:
            terms.append(f'{value}*x^{key}')
        else:
            terms.append(f'{value}')
    return ' + '.join(reversed(terms))


def write_to_file_polynom(file_name: str, polynom: str):
    with open(file_name, 'w') as f:
        f.write(polynom)


if __name__ == "__main__":


    MIN_COEFF = 1
    MAX_COEFF = 100
    POW = 10


    pol = generate_polynom(POW, MIN_COEFF, MAX_COEFF)
    pol_s = stringify_polynom(pol)
    write_to_file_polynom('pol.txt', pol_s)


    pol1 = generate_polynom_dict(POW, MIN_COEFF, MAX_COEFF)
    pol1_s = stringify_polynom_dict(pol1)
    write_to_file_polynom('pol1.txt', pol1_s)
