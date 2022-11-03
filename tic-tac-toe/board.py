BOARD_TEMPLATE = """
╔═══╤═══╤═══╗
║ * │ * │ * ║
╟───┼───┼───╢
║ * │ * │ * ║
╟───┼───┼───╢
║ * │ * │ * ║
╚═══╧═══╧═══╝
"""


def create_board(brd: list, board_template: str = BOARD_TEMPLATE, sym: str = '*') -> str:
    result = board_template
    for el in brd:
        if not el:
            result = result.replace(sym, ' ', 1)
        else:
            result = result.replace(sym, el, 1)
    return result
