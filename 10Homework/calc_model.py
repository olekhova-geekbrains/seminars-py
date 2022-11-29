##https://habr.com/ru/post/50196/

from operator import add, sub, mul, truediv
from typing import Union

generic_number = Union[int, float]


def parse_string(expr_str: str) -> list:
    """
    Функция парсинга строки, выделения операторов, операндов и занесения их в список
    Работает с операторами /*-+
    Работает с операндами: целые числа
    TODO Добавить скобочки, возведение в степень, рациональные числа вида 1.23
    :param expr_str: Строка для парсинга
    :return: Список
    """
    rez = []
    start_digit = 0
    for idx, el in enumerate(expr_str):
        if el in '()/*-+':
            number_string = expr_str[start_digit:idx]
            if number_string != "": rez.append(int(number_string))
            rez.append(el)
            start_digit = idx + 1
    number_string = expr_str[start_digit:]
    if number_string != "": rez.append(int(number_string))
    return rez


def one_calc(op: str, prev_el: int, next_el: int) -> int:
    """
    Выполнение одного арифметического действия и возвращение результата
    :param op: Оператор в в виде строки
    :param prev_el: Операнд 1
    :param next_el: Операнд 2
    :return: результат выполнения в виде int
    """
    if op == "*":
        return prev_el * next_el
    elif op == "/":
        return prev_el / next_el
    elif op == "+":
        return prev_el + next_el
    elif op == "-":
        return prev_el - next_el
    else:
        raise TypeError("Некорректная операция")


def operation_calc(expr_list: list, operations: str) -> list:
    """
    Выполнение арифмитических операций для заданного распарсенного списка
    :param expr_list: Список операций и операндов
    :param operations: Операции в виде строки: "*/"  "-+"
    :return: Копию исходного списка, с произведенными заменами выполненных операций на соответствующие результаты
    """
    tmp_list = expr_list.copy()
    idx = 1
    lenght = len(tmp_list) - 1
    while idx <= lenght:  # Здесь цикл for подойдет плохо
        el = tmp_list[idx]
        if str(el) in operations:
            result = one_calc(el, tmp_list[idx - 1], tmp_list[idx + 1])
            tmp_list[idx] = result
            tmp_list.pop(idx + 1)
            tmp_list.pop(idx - 1)
            lenght -= 2
        else:
            idx += 1
    return tmp_list


def total_calc(expr_list: list) -> generic_number:
    tmp_list = expr_list.copy()
    while True:
        if "(" in tmp_list:
            parent_open = tmp_list.index("(")
            parent_close = tmp_list.index(")", parent_open)
            parent_expression = tmp_list[parent_open + 1: parent_close]
            in_parent_list = operation_calc(parent_expression, "*/")
            in_parent_list = operation_calc(in_parent_list, "-+")
            tmp_list[parent_open] = in_parent_list[0]
            tmp_list[parent_open+1: parent_close+1 ] = []
        else: break
    tmp_list = operation_calc(tmp_list, "*/")
    tmp_list = operation_calc(tmp_list, "-+")
    return tmp_list[0]


def calculate(expr_str: str)-> generic_number:
    return total_calc(parse_string(expr_str))

