"""
Файл тестирования функций: заход на автотесты

"""

import less06_task41_ariphmetic as code


def error_message(callback, test_data, result, require_result):
    print(f"Функция {callback.__name__}: ERROR in {test_data}: Получено {result}  Ожидалось: {require_result}")


def pass_message(callback, test_data, result, require_result):
    print(f"Функция {callback.__name__}: PASS in {test_data}: Получено {result}  Ожидалось: {require_result}")


def test_callback(callback, tests_data):
    for test, require in tests_data:
        result = callback(*test)
        if result != require:
            error_message(callback, test, result, require)
        else:
            pass_message(callback, test, result, require)


# '2+2'           ->  4
# '1+2*3'         ->  7
# '1-2*3'         -> -5
# '1-2*33'        -> -65
# '2-1+3*7'       -> 10
# '1-2*3/5'       -> -0.2
# '1+2*3-6*5+78'  -> 55

parse_string_tests = [
    [('2+2',), [2, '+', 2]],
    [('1+2*3',), [1, '+', 2, '*', 3]],
    [('1-2*3',), [1, '-', 2, '*', 3]],
    [('1-2*33',), [1, '-', 2, '*', 33]],
    [('2-1+3*7',), [2, '-', 1, '+', 3, '*', 7]],
    [('1-2*3/5',), [1, '-', 2, '*', 3, '/', 5]],
    [('1+2*3-6*5+78',), [1, '+', 2, '*', 3, '-', 6, '*', 5, '+', 78]],
    [('6/10*10+4',), [6, '/', 10, '*', 10, '+', 4]],
    [('(11+2/7)',), ['(', 11, '+', 2, '/', 7, ')']],
    [('(11+2)/7',), ['(', 11, '+', 2, ')', '/', 7]],
    [('(1+2)*3-6*(5+78)',), ['(', 1, '+', 2, ')', '*', 3, '-', 6, '*', '(', 5, '+', 78, ')']],

]

test_callback(code.parse_string, parse_string_tests)

# [[(i[1],), None] for i in parse_string_tests ]
# code. total_calc
calculate_tests = [
    [([2, '+', 2],), 4],
    [([1, '+', 2, '*', 3],), 7],
    [([1, '-', 2, '*', 3],), -5],
    [([1, '-', 2, '*', 33],), -65],
    [([2, '-', 1, '+', 3, '*', 7],), 22],
    [([1, '-', 2, '*', 3, '/', 5],), -0.19999999999999996],
    [([1, '+', 2, '*', 3, '-', 6, '*', 5, '+', 78],), 55],
    [([6, '/', 10, '*', 10, '+', 4],), 10],
    [(['(', 11, '+', 2, '/', 7, ')'],), 11.285714285714286],
    [(['(', 11, '+', 2, ')', '/', 7],), 1.8571428571428572],
    [(['(', 1, '+', 2, ')', '*', 3, '-', 6, '*', '(', 5, '+', 78, ')'],), -489],
]
test_callback(code.total_calc, calculate_tests)
