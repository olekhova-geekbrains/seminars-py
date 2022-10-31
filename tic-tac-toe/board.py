from colorama import Fore, Style
from colorama import init
init(autoreset=True)

BOARD_TEMPLATE = """
╔═══╤═══╤═══╗
║ * │ * │ * ║
╟───┼───┼───╢
║ * │ * │ * ║
╟───┼───┼───╢
║ * │ * │ * ║
╚═══╧═══╧═══╝
"""


# def create_board(brd: list, board_template: str = BOARD_TEMPLATE, sym: str = '*') -> str:
#     result = board_template
#     for row in brd:
#         for cell in row:
#             result = result.replace(sym, cell, 1)
#     return result


def create_board(brd: list, board_template: str = BOARD_TEMPLATE, sym: str = '*') -> str:
    result = board_template
    for el in brd:
        result = result.replace(sym, el, 1)
    return result


def create_board_victory(brd: list, vct_line: list, board_template: str = BOARD_TEMPLATE, sym: str = '*') -> str:
    result = board_template
    for el in brd:
        if el in vct_line:
            color_el = Fore.GREEN + el + Style.RESET_ALL
            #print(Style.RESET_ALL)
            result = result.replace(sym, color_el, 1)
        else:
            result = result.replace(sym, el, 1)
    return result
