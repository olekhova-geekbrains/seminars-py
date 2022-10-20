# 5. (Усложненное). Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Выделите необходимые действия, этапы алгоритма. Посмотрите какие из них уже решены в предыдущей задаче.
# Оформите необходимые функции в виде модуля и импортируйте.
# Примечание Многочлены в файлах могут быть разной степени

from task4_polynom import stringify_polynom_dict, write_to_file_polynom


def read_from_file_polynom(file_name: str):
    with open(file_name, 'r') as f:
        polynom_s = f.read()
    return polynom_s

def parse_polynom(pl: str) -> dict:
    terms = pl.split(" + ")
    coeffs = {}
    for el in terms:
        if "^" not in el:
            coeffs[0] = int(el)
        else:
            pow_el = int(el.split("^")[1])
            coeff_el = int(el.split("*")[0])
            coeffs[pow_el] = coeff_el
    return coeffs


def sum_polynoms(pl1: dict, pl2: dict) -> dict:
    sum_value = pl1
    result = pl2
    for key1 in pl1.keys():
        if key1 in pl2.keys():
            sum_value[key1] += pl2[key1]
    result.update(sum_value)
    return result

pol = read_from_file_polynom('./pol1.txt')
pol_dict = parse_polynom(pol)
print(pol)
print(pol_dict)


pol1 = read_from_file_polynom('./pol2.txt')
pol1_dict = parse_polynom(pol1)
print()
print(pol1)
print(pol1_dict)


sum_pol = sum_polynoms(pol_dict, pol1_dict)
print()
print(sum_pol)


sum_pol_s = stringify_polynom_dict(sum_pol)
write_to_file_polynom('sum_pol.txt', sum_pol_s)